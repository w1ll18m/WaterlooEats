from flask_restful import Resource
from flask import request, jsonify
from ..database.product_tags import ProductTags
from ..database.product import Product
from ..database.tags import Tag
from ..api_endpoints.auth_handler import token_required, scope_required
from ..extensions import db

class ListProductByTag(Resource):
    @token_required
    def post(self, tag_id):
        existing_entries = ProductTags.query.filter_by(tag_id=tag_id)

        paginated_page_num = request.form.get("page_num")
        if paginated_page_num: paginated_page_num = int(paginated_page_num)
        paginated_items_per = request.form.get("items_per")
        if paginated_items_per: paginated_items_per = int(paginated_items_per)
        
        if paginated_page_num and paginated_items_per:
            existing_entries = existing_entries.paginate(page=paginated_page_num, per_page=paginated_items_per).items
        else:
            existing_entries = existing_entries.all()

        product_list = []

        for entry in existing_entries:
            product_list.append(entry.product)
        
        product_obj_list = []

        for product in product_list:
            product_obj = {
                "product_id": product.product_id, 
                "product_name": product.product_name, 
                "description": product.description, 
                "price": product.price, 
                "calorie_count": product.calorie_count, 
                "image_url": product.image_url,
                "resteraunt_id": product.resteraunt_id
            }

            product_obj_list.append(product_obj)

        return jsonify(product_obj_list)

class ListTagByProduct(Resource):
    @token_required
    def get(self, product_id):
        existing_entries = ProductTags.query.filter_by(product_id=product_id).all()

        tag_list = []

        for entry in existing_entries:
            tag_list.append(entry.tag)
        
        tag_obj_list = []

        for tag in tag_list:
            tag_obj = {
                "tag_id": tag.tag_id, 
                "tag_name": tag.tag_name, 
                "resteraunt_id": tag.resteraunt_id
            }

            tag_obj_list.append(tag_obj)

        return jsonify(tag_obj_list)

class ProductTagPost(Resource):
    @scope_required(["write:data"])
    def post(self):
        new_product_id = request.form.get("product_id")
        if not new_product_id:
            return "Please provide field 'product_id'."
        existing_product = Product.query.get(new_product_id)
        if not existing_product:
            return f"Product wth 'product_id' {new_product_id} does not exist."
        
        new_tag_id = request.form.get("tag_id")
        if not new_tag_id:
            return "Please provide field 'tag_id'."
        existing_tag = Tag.query.get(new_tag_id)
        if not existing_tag:
            return f"Tag wth 'tag_id' {new_tag_id} does not exist."
        
        existing_entries = ProductTags.query.filter_by(product_id=new_product_id)
        existing_entry = existing_entries.filter_by(tag_id=new_tag_id).first()
        if existing_entry:
            return f"Entry with product_id '{new_product_id}' and tag_id '{new_tag_id}' already exists."
        
        new_entry = ProductTags(new_product_id, new_tag_id)
        db.session.add(new_entry)
        db.session.commit()

        return f"Entry with name product_id '{new_product_id}' and tag_id '{new_tag_id}' succesfully created."

class ProductTagDelete(Resource):
    @scope_required(["delete:data"])
    def delete(self, product_id, tag_id):
        existing_entries = ProductTags.query.filter_by(tag_id=tag_id).all()
        existing_entry = existing_entries.filter_by(product_id=product_id).first()
        if not existing_entry:
            return f"Entry with name product_id '{product_id}' and tag_id '{tag_id}' does not exist."
        
        db.session.delete(existing_entry)
        db.session.commit()

        return f"Entry with name product_id '{product_id}' and tag_id '{tag_id}' sucessfully deleted"