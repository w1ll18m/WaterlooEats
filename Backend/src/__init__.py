from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    DB_NAME = 'waterlooeats.db'

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # SECRET_KEY is used for JWT token authentication
    app.config['SECRET_KEY'] = "d05bd4c933fe2564f580c72ac717a02749deaba4158d31544836aa6043f34ddf"
    # enables for cross origin resource sharing for api routes
    CORS(app) 

    db.init_app(app)
    
    # the following snippet of code is used to enable foreign key support for SQLite databases
    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
            dbapi_con.execute('pragma foreign_keys=ON')

        with app.app_context():
            from sqlalchemy import event
            event.listen(db.engine, 'connect', _fk_pragma_on_connect)

    api = Api(app)

    from .database.product import Product
    from .database.tags import Tag
    from .database.product_tags import ProductTags
    from .database.resteraunt import Resteraunt
    from .database.hours import Hour
    from .database.resteraunt_owner import ResterauntOwner

    with app.app_context():
        db.create_all()
        print("Created Database")

        # db.drop_all() -> for testing purposes

    from .api.api_routing import Routes

    routes = Routes(app, api)
    routes.setRoutes()

    return app