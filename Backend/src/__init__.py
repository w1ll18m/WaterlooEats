from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    DB_NAME = 'waterlooeats.db'
    SECRET_KEY = 'temporary_key'

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = SECRET_KEY
    CORS(app) # enables for cross origin resource sharing for api routes

    db.init_app(app)

    api = Api(app)

    from .database.product import Product
    from .database.tags import Tag
    from .database.product_tags import ProductTags

    with app.app_context():
        db.create_all()
        print("Created Database")

        # db.drop_all() -> for testing purposes

    from .api.api_routing import Routes

    routes = Routes()
    route_list = routes.getRoutes()

    for route in route_list:
        api.add_resource(route["class"], route["route_url"])

    @app.route('/')
    def home():
        return "This is just to test various features"

    return app