from .product_handler import *
from .tag_handler import *
from .product_tags_handler import *

class Routes():
    def __init__(self):
        self.routes = [
            {"class": ProductListAll, "route_url": "/product/list/<int:resteraunt_id>"},
            {"class": ProductPost, "route_url": "/product/add"},
            {"class": ProductDelete, "route_url": "/product/delete/<int:product_id>"},
            {"class": ProductDeleteByName, "route_url": "/product.deleteByName/<string:product_name>"},

            {"class": TagListAll, "route_url": "/tag/list/<int:resteraunt_id>"},
            {"class": TagPost, "route_url": "/tag/add"},
            {"class": TagDelete, "route_url": "/tag/delete/<int:tag_id>"},

            {"class": ListProductByTag, "route_url": "/product-tags/list-product-by-tag/<int:tag_id>"},
            {"class": ListTagByProduct, "route_url": "/product-tags/list-tag-by-product/<int:product_id>"},
            {"class": ProductTagPost, "route_url": "/product-tags/add"},
            {"class": ProductTagDelete, "route_url": "/product-tags/delete/<int:product_id>/<int:tag_id>"}
        ]
    
    def getRoutes(self):
        return self.routes