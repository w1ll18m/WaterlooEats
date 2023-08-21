from flask import Flask, render_template
from flask_restful import Api, Resource
from flask_cors import CORS
from .extensions import db, api
from .api_endpoints.api_routing import Routes

def create_app():
    DB_NAME = 'waterlooeats.db'

    # =============================================================================
    # Set up flask application settings/configurations
    # =============================================================================
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # SECRET_KEY is used for JWT token authentication
    app.config['SECRET_KEY'] = "d05bd4c933fe2564f580c72ac717a02749deaba4158d31544836aa6043f34ddf"
    app.config['CELERY_RESULT_BACKEND'] = "redis://localhost:6379/0"
    app.config['CELERY_BROKER_URL'] = "pyamqp://guest@localhost//"
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

    # =============================================================================
    # Set up database models
    # =============================================================================

    from .database.product import Product
    from .database.tags import Tag
    from .database.product_tags import ProductTags
    from .database.resteraunt import Resteraunt
    from .database.hours import Hour
    from .database.resteraunt_owner import ResterauntOwner
    from .database.user import User

    with app.app_context():
        # db.drop_all() -> for testing purposes
        db.create_all()
        print("Created Database")

    # =============================================================================
    # Set up restful api endpoints
    # =============================================================================

    routes = Routes(api)
    routes.setRoutes()

    api.init_app(app)

    return app