from flask_restful import Resource
from flask import request, jsonify
from ..database.product import Product
from ..database.resteraunt import Resteraunt
from .. import db

class ProductListAll(Resource):
    def post(self, resteraunt_id):
        existing_products = Product.query.filter_by(resteraunt_id=resteraunt_id)

        paginated_page_num = request.form.get("page_num")
        if paginated_page_num: paginated_page_num = int(paginated_page_num)
        paginated_items_per = request.form.get("items_per")
        if paginated_items_per: paginated_items_per = int(paginated_items_per)

        if paginated_page_num and paginated_items_per:
            existing_products = existing_products.paginate(page=paginated_page_num, per_page=paginated_items_per).items
        else:
            existing_products = existing_products.all()

        product_list = []

        for product in existing_products:
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
        existing_resteraunt = Resteraunt.query.get(new_resteraunt_id)
        if not existing_resteraunt:
            return f"Resteraunt wth 'resteraunt_id' {new_resteraunt_id} does not exist."
        
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




