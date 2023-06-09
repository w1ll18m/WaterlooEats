from flask_restful import Resource
from flask import request, jsonify
from ..database.product import Product
from .. import db

class ProductListAll(Resource):
    def get(self):
        resteraunt_id = request.form.get("resteraunt_id")
        if not resteraunt_id:
            return "Please provide field 'resteraunt_id'."
        
        existing_products = Product.query.filter_by(resteraunt_id=resteraunt_id).all()

        product_list = []

        for product in existing_products:
            product_obj = {
                "product_id": product.product_id, 
                "product_name": product.product_name, 
                "description": product.description, 
                "price": product.price, 
                "calorie_count": product.calorie_count, 
                "image_url": product.image_url
            }

            product_list.append(product_obj)

        return product_list

class ProductPost(Resource):
    def post(self):
        new_product_name = request.form.get("product_name")
        if not new_product_name:
            return "Please provide field 'product_name'."
        new_product_name = str(new_product_name).strip()

        existing_product = Product.query.filter_by(product_name=new_product_name).first()
        if existing_product:
            return f"Product with product_name '{new_product_name}' already exists."

        new_description = request.form.get("description")
        if not new_description:
            new_description = ""
        new_description = str(new_description).strip()

        new_price = request.form.get("price")
        if not new_price:
            return "Please provide field 'price'."

        new_calorie_count = request.form.get("calorie_count")
        if not new_calorie_count:
            return "Please provide field 'calorie_count'."

        new_image_url = request.form.get("image_url")
        if not new_image_url:
            new_image_url = ""
        new_image_url = str(new_image_url).strip()

        new_resteraunt_id = request.form.get("resteraunt_id")
        if not new_resteraunt_id:
            return "Please provide field 'resteraunt_id'."
        
        new_product = Product(new_product_name, new_description, new_price, new_calorie_count, new_image_url, new_resteraunt_id)
        db.session.add(new_product)
        db.session.commit()

        return f"Product with name '{new_product_name}' succesfully created."
    
class ProductDelete(Resource):
    def delete(self, product_id):
        existing_product = Product.query.filter_by(product_id=product_id).first()
        if not existing_product:
            return f"Product with id '{product_id}' does not exist."
        
        db.session.delete(existing_product)
        db.session.commit()

        return f"Product with id '{product_id}' sucessfully deleted"

class ProductDeleteByName(Resource):
    def delete(self, product_name):
        existing_product = Product.query.filter_by(product_name=product_name).first()
        if not existing_product:
            return f"Product with name '{product_name}' does not exist."
        
        db.session.delete(existing_product)
        db.session.commit()

        return f"Product with name '{product_name}' sucessfully deleted"



