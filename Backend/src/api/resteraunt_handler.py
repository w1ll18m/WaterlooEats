from flask_restful import Resource
from flask import request, jsonify, make_response, Response
from ..utils.redis_client import getOrSetCache
from ..database.resteraunt import Resteraunt
from ..api.auth_handler import token_required, scope_required
from ..database.hours import Hour
from .. import db

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
            return make_response("Please prvoide field 'closing_hours'.", 400)
        new_closing_hours = str(new_closing_hours).strip()
        
        new_resteraunt = Resteraunt(new_resteraunt_name, new_cuisine_type, new_location, new_description, new_image_url, new_delivery_fee)
        db.session.add(new_resteraunt)
        db.session.commit()

        new_resteraunt_id = Resteraunt.query.filter_by(resteraunt_name=new_resteraunt_name).first().resteraunt_id
        new_hour = Hour(new_resteraunt_id, new_opening_hours, new_closing_hours)
        db.session.add(new_hour)
        db.session.commit()

        return make_response(f"Resteraunt with name '{new_resteraunt_name}' succesfully created.", 200)

class ResterauntDelete(Resource):
    @scope_required(["delete:data"])
    def delete(self, resteraunt_id):
        existing_resteraunt = Resteraunt.query.get(resteraunt_id)
        if not existing_resteraunt:
            return make_response(f"Resteraunt with id '{resteraunt_id}' does not exist.", 404)
        
        db.session.delete(existing_resteraunt)
        db.session.commit()

        return make_response(f"Resteraunt with id '{resteraunt_id}' sucessfully deleted", 200)