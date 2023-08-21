import os
import json
import redis
from dotenv import load_dotenv
from celery import shared_task
from flask_restful import Resource
from flask import request, jsonify, make_response, current_app, Response
from ..utils.redis_client import getOrSetCache
from ..database.resteraunt import Resteraunt
from ..api_endpoints.auth_handler import token_required, scope_required
from ..database.hours import Hour
from ..extensions import db

load_dotenv()
DEFAULT_EXPIRATION_TIME = 3600
redis_server_host = os.getenv("REDIS_SERVER_HOST")
redis_server_port = os.getenv("REDIS_SERVER_PORT")
redis_client = redis.StrictRedis(host=redis_server_host, port=redis_server_port, db=0)

class ResterauntGet(Resource):
    @token_required
    def get(self, resteraunt_id):
        def queryResteraunt():
            existing_resteraunt = Resteraunt.query.get(resteraunt_id)
            if not existing_resteraunt:
                return make_response(f"Resteraunt with 'resteraunt_id' {resteraunt_id} does not exist.", 404)
            
            resteraunt_obj = {
                "resteraunt_name": existing_resteraunt.resteraunt_name,
                "cuisine_type": existing_resteraunt.cuisine_type,
                "location": existing_resteraunt.location,
                "description": existing_resteraunt.description,
                "delivery_fee": existing_resteraunt.delivery_fee,
                "image_url": existing_resteraunt.image_url,
                "opening_hours": existing_resteraunt.hour.opening_hours,
                "closing_hours": existing_resteraunt.hour.closing_hours
            }

            return resteraunt_obj
        
        query_key = f"resteraunt-get:{resteraunt_id}"
        query_response = getOrSetCache(query_key, queryResteraunt)

        if isinstance(query_response, Response):
            return query_response
        return make_response(jsonify(query_response), 200)  

class ResterauntList(Resource):
    def get(self):
        def queryResterauntList():
            existing_resteraunts = Resteraunt.query.all()

            resteraunt_list = []
            for resteraunt in existing_resteraunts:
                resteraunt_obj = {
                    "resteraunt_name": resteraunt.resteraunt_name,
                    "cuisine_type": resteraunt.cuisine_type,
                    "location": resteraunt.location,
                    "description": resteraunt.description,
                    "delivery_fee": resteraunt.delivery_fee,
                    "image_url": resteraunt.image_url,
                    "opening_hours": resteraunt.hour.opening_hours,
                    "closing_hours": resteraunt.hour.closing_hours
                }
                resteraunt_list.append(resteraunt_obj)

            return resteraunt_list
        
        query_key = "resteraunt-list"
        query_response = getOrSetCache(query_key, queryResterauntList)

        if isinstance(query_response, Response):
            return query_response
        return make_response(jsonify(query_response), 200)  

class ResterauntPost(Resource):
    @scope_required(["write:data"])
    def post(self):
        new_resteraunt_name = request.form.get("resteraunt_name")
        if not new_resteraunt_name:
            return make_response("Please provide field 'resteraunt_name'.", 400)
        new_resteraunt_name = str(new_resteraunt_name).strip()

        existing_resteraunt = Resteraunt.query.filter_by(resteraunt_name=new_resteraunt_name).first()
        if existing_resteraunt:
            return make_response(f"Resteraunt with resteraunt_name '{new_resteraunt_name}' already exists.", 409)
        
        new_cuisine_type = request.form.get("cuisine_type")
        if not new_cuisine_type:
            return make_response("Please provide field 'cuisine_type'.", 400)
        new_cuisine_type = str(new_cuisine_type).strip()

        new_location = request.form.get("location")
        if not new_location:
            return make_response("Please provide field 'location'.", 400)
        new_location = str(new_location).strip()

        new_description = request.form.get("description")
        if not new_description:
            new_description = ""
        new_description = str(new_description).strip()

        new_delivery_fee = request.form.get("delivery_fee")
        if not new_delivery_fee:
            return make_response("Please provide field 'delivery_fee'.", 400)

        new_image_url = request.form.get("image_url")
        if not new_image_url:
            new_image_url = ""
        new_image_url = str(new_image_url).strip()  

        new_opening_hours = request.form.get("opening_hours")
        if not new_opening_hours:
            return make_response("Please provide field 'opening_hour'.", 400)
        new_opening_hours = str(new_opening_hours).strip()

        new_closing_hours = request.form.get("closing_hours")
        if not new_closing_hours:
            return make_response("Please provide field 'closing_hours'.", 400)
        new_closing_hours = str(new_closing_hours).strip()

        # Write to the Cache First in Write Through Pattern (Need to Write to ResterauntList Cached Data)
        resteraunt_list_data = redis_client.get("resteraunt-list")
        if resteraunt_list_data is not None:
            resteraunt_list_data = json.loads(resteraunt_list_data)
            new_resteraunt = {
                "resteraunt_name": new_resteraunt_name,
                "cuisine_type": new_cuisine_type,
                "location": new_location,
                "description": new_description,
                "delivery_fee": new_delivery_fee,
                "image_url": new_image_url,
                "opening_hours": new_opening_hours,
                "closing_hours": new_closing_hours
            }
            resteraunt_list_data.append(new_resteraunt)
            redis_client.setex("resteraunt-list", DEFAULT_EXPIRATION_TIME, json.dumps(resteraunt_list_data))

        # Write to the Database Second in Write Through Pattern
        new_resteraunt = Resteraunt(new_resteraunt_name, new_cuisine_type, new_location, new_description, new_image_url, new_delivery_fee)
        db.session.add(new_resteraunt)
        db.session.commit()

        new_resteraunt_id = Resteraunt.query.filter_by(resteraunt_name=new_resteraunt_name).first().resteraunt_id
        new_hour = Hour(new_resteraunt_id, new_opening_hours, new_closing_hours)
        db.session.add(new_hour)
        db.session.commit()

        return make_response(f"Resteraunt with name '{new_resteraunt_name}' succesfully created.", 200)

@shared_task
def deleteResterauntFromDB(resteraunt_id):
    existing_resteraunt = Resteraunt.query.get(resteraunt_id)
    if not existing_resteraunt:
        response = {
            "message": f"Resteraunt with id '{resteraunt_id}' does not exist.",
            "code": 404,
            "status": False
        }
        return response
        
    db.session.delete(existing_resteraunt)
    db.session.commit()

    response = {
        "message": f"Resteraunt with id '{resteraunt_id}' successfully deleted.",
        "code": 200,
        "status": True
    }
    return response

class ResterauntDelete(Resource):
    @scope_required(["delete:data"])
    def delete(self, resteraunt_id):
        # Write to the Cache First in Write Through Pattern (Need to Write to ResterauntList, ResterauntGet Cached Data)
        resteraunt_list_data = redis_client.get("resteraunt-list")
        if resteraunt_list_data is not None:
            resteraunt_list_data = json.loads(resteraunt_list_data)
            for index, value in enumerate(resteraunt_list_data):
                resteraunt_list_data.pop(index)
            redis_client.setex("resteraunt-list", DEFAULT_EXPIRATION_TIME, json.dumps(resteraunt_list_data))
            redis_client.delete("resteraunt-list")
        
        resteraunt_get_data = redis_client.get(f"resteraunt-get:{resteraunt_id}")
        if resteraunt_get_data is not None:
            resteraunt_get_data = json.loads(resteraunt_get_data)
            redis_client.delete(f"resteraunt-get:{resteraunt_id}")

        # Write to the Database Second in Write Through Pattern
        query_response = deleteResterauntFromDB.delay(resteraunt_id)

        if isinstance(query_response, Response):
            return query_response

        return make_response(f"Resteraunt with id '{resteraunt_id}' sucessfully deleted", 200)