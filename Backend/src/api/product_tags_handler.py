from flask_restful import Resource
from flask import request, jsonify
from ..database.product_tags import ProductTags
from ..database.product import Product
from ..database.tags import Tag
from .. import db

class ListProductByTag(Resource):
    def get(self, tag_id):
        existing_entries = ProductTags.query.filter_by(tag_id=tag_id).all()

        product_id_list = []

        for entry in existing_entries:
            product_id_list.append(entry.product_id)
        
        product_list = []

        for product_id in product_id_list:
            product = Product.query.get(product_id)

            product_obj = {
                "product_id": product.product_id, 
                "product_name": product.product_name, 
                "description": product.description, 
                "price": product.price, 
                "calorie_count": product.calorie_count, 
                "image_url": product.image_url,
                "resteraunt_id": product.resteraunt_id
            }

            product_list.append(product_obj)

        return jsonify(product_list)

class ListTagByProduct(Resource):
    def get(self, product_id):
        existing_entries = ProductTags.query.filter_by(product_id=product_id).all()

        tag_id_list = []

        for entry in existing_entries:
            tag_id_list.append(entry.tag_id)
        
        tag_list = []

        for tag_id in tag_id_list:
            tag = Tag.query.get(tag_id)

            tag_obj = {
                "tag_id": tag.tag_id, 
                "tag_name": tag.tag_name, 
                "resteraunt_id": tag.resteraunt_id
            }

            tag_list.append(tag_obj)

        return jsonify(tag_list)

class ProductTagPost(Resource):
    def post(self):
        new_product_id = request.form.get("product_id")
        if not new_product_id:
            return "Please provide field 'product_id'."
        
        new_tag_id = request.form.get("tag_id")
        if not new_tag_id:
            return "Please provide field 'tag_id'."
        
        existing_entries = ProductTags.query.filter_by(product_id=new_product_id)
        existing_entry = existing_entries.filter_by(tag_id=new_tag_id).first()
        if existing_entry:
            return f"Entry with product_id '{new_product_id}' and tag_id '{new_tag_id}' already exists."
        
        new_entry = ProductTags(new_product_id, new_tag_id)
        db.session.add(new_entry)
        db.session.commit()

        return f"Entry with name product_id '{new_product_id}' and tag_id '{new_tag_id}' succesfully created."

class ProductTagDelete(Resource):
    def delete(self, product_id, tag_id):
        existing_entries = ProductTags.query.filter_by(tag_id=tag_id).all()
        existing_entry = existing_entries.filter_by(product_id=product_id).first()
        if not existing_entry:
            return f"Entry with name product_id '{product_id}' and tag_id '{tag_id}' does not exist."
        
        db.session.delete(existing_entry)
        db.session.commit()

        return f"Entry with name product_id '{product_id}' and tag_id '{tag_id}' sucessfully deleted"