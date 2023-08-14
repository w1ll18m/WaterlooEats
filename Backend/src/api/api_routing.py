from .product_handler import *
from .tag_handler import *
from .product_tags_handler import *
from .resteraunt_handler import *
from .auth_handler import *

class Routes():
    def __init__(self, flask_app, flask_api):
        self.routes = [
            {"class": ResterauntPost, "route_url": "/resteraunt/add"}, # POST
            {"class": ResterauntGet, "route_url": "/resteraunt/get/<int:resteraunt_id>"}, # GET
            {"class": ResterauntDelete, "route_url": "/resteraunt/delete/<int:resteraunt_id>"}, # DELETE

            {"class": ProductListAll, "route_url": "/product/list/<int:resteraunt_id>"}, # POST
            {"class": ProductPost, "route_url": "/product/add"}, # POST
            {"class": ProductDelete, "route_url": "/product/delete/<int:product_id>"}, # DELETE
            {"class": ProductDeleteByName, "route_url": "/product.deleteByName/<string:product_name>"}, # DELETE

            {"class": TagListAll, "route_url": "/tag/list/<int:resteraunt_id>"}, # GET
            {"class": TagPost, "route_url": "/tag/add"}, # POST
            {"class": TagDelete, "route_url": "/tag/delete/<int:tag_id>"}, # DELETE

            {"class": ListProductByTag, "route_url": "/product-tags/list-product-by-tag/<int:tag_id>"}, # POST
            {"class": ListTagByProduct, "route_url": "/product-tags/list-tag-by-product/<int:product_id>"}, # GET
            {"class": ProductTagPost, "route_url": "/product-tags/add"}, # POST
            {"class": ProductTagDelete, "route_url": "/product-tags/delete/<int:product_id>/<int:tag_id>"}, # DELETE

            {"class": CheckExistingUser, "route_url": "/auth/check-existing-user"}, # POST
            {"class": CreateNewUser, "route_url": "/auth/create-user"}, # POST
            {"class": ValidateAuth0Token, "route_url": "/auth/checkauth0"}, # GET

            # THE FOLLOWING ROUTES WERE USED FOR OLD JWT TOKEN AUTHENTICATION SYSTEM:
            # {"class": SignUpUser, "route_url": "/auth/add-user"}, # POST
            # {"class": Login, "route_url": "/auth/login"}, # POST
            # {"class": ValidateJWTToken, "route_url": "/auth/checkjwt"}, # GET
            # {"class": ValidateExistingUser, "route_url": "/auth/checkuser"}, # POST
        ]

        self.flask_app = flask_app
        self.flask_api = flask_api
    
    def setRoutes(self):
        for route in self.routes:
            self.flask_api.add_resource(route["class"], route["route_url"])