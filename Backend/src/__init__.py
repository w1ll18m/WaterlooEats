from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def create_app():
    DB_NAME = 'waterlooeats.db'
    SECRET_KEY = 'temporary_key'

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = SECRET_KEY

    db.init_app(app)

    api = Api(app)

    from .database import product

    with app.app_context():
        db.create_all()
        print("Created Database")

    from .api.product_handler import ProductListAll, ProductPost, ProductDelete, ProductDeleteByName
    api.add_resource(ProductListAll, "/product/list")
    api.add_resource(ProductPost, "/product/add")
    api.add_resource(ProductDelete, "/product/deleteByID/<int:product_id>")
    api.add_resource(ProductDeleteByName, "/product.deleteByName/<string:product_name>")

    @app.route('/')
    def home():
        return "This is just to test various features"

    return app