from flask_restful import Resource
from flask import request, jsonify, make_response
from ..database.tags import Tag
from ..database.resteraunt import Resteraunt
from ..api.auth_handler import token_required, scope_required
from .. import db

class TagListAll(Resource):
    @token_required
    def get(self, resteraunt_id):
        existing_tags = Tag.query.filter_by(resteraunt_id=resteraunt_id).all()

        tag_list = []

        for tag in existing_tags:
            tag_obj = {
                "tag_id": tag.tag_id, 
                "tag_name": tag.tag_name,
                "resteraunt_id": tag.resteraunt_id
            }

            tag_list.append(tag_obj)

        return jsonify(tag_list)

class TagPost(Resource):
    @scope_required(["write:data"])
    def post(self):
        new_tag_name = request.form.get("tag_name")
        if not new_tag_name:
            return make_response("Please provide field 'tag_name'.", 400)
        new_tag_name = str(new_tag_name).strip()

        existing_tag = Tag.query.filter_by(tag_name=new_tag_name).first()
        if existing_tag:
            return make_response(f"Tag with tag_name '{new_tag_name}' already exists.", 409)

        new_resteraunt_id = request.form.get("resteraunt_id")
        if not new_resteraunt_id:
            return make_response("Please provide field 'resteraunt_id'.", 400)
        existing_resteraunt = Resteraunt.query.get(new_resteraunt_id)
        if not existing_resteraunt:
            return make_response(f"Resteraunt wth 'resteraunt_id' {new_resteraunt_id} does not exist.", 404)
        
        new_tag = Tag(new_tag_name, new_resteraunt_id)
        db.session.add(new_tag)
        db.session.commit()

        return make_response(f"Tag with name '{new_tag_name}' succesfully created.", 200)
    
class TagDelete(Resource):
    @scope_required(["delete:data"])
    def delete(self, tag_id):
        existing_tag = Tag.query.filter_by(tag_id=tag_id).first()
        if not existing_tag:
            return make_response(f"Tag with id '{tag_id}' does not exist.", 404)
        
        db.session.delete(existing_tag)
        db.session.commit()

        return make_response(f"Tag with id '{tag_id}' sucessfully deleted", 200)




