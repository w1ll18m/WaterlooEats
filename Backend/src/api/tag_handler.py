from flask_restful import Resource
from flask import request, jsonify
from ..database.tags import Tag
from .. import db

class TagListAll(Resource):
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
    def post(self):
        new_tag_name = request.form.get("tag_name")
        if not new_tag_name:
            return "Please provide field 'tag_name'."
        new_tag_name = str(new_tag_name).strip()

        existing_tag = Tag.query.filter_by(tag_name=new_tag_name).first()
        if existing_tag:
            return f"Tag with tag_name '{new_tag_name}' already exists."

        new_resteraunt_id = request.form.get("resteraunt_id")
        if not new_resteraunt_id:
            return "Please provide field 'resteraunt_id'."
        
        new_tag = Tag(new_tag_name, new_resteraunt_id)
        db.session.add(new_tag)
        db.session.commit()

        return f"Tag with name '{new_tag_name}' succesfully created."
    
class TagDelete(Resource):
    def delete(self, tag_id):
        existing_tag = Tag.query.filter_by(tag_id=tag_id).first()
        if not existing_tag:
            return f"Tag with id '{tag_id}' does not exist."
        
        db.session.delete(existing_tag)
        db.session.commit()

        return f"Tag with id '{tag_id}' sucessfully deleted"




