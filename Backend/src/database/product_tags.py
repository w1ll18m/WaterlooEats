from .. import db

class ProductTags(db.Model): # Many-to-Many relationship between Product and Tag
    product_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=False
    )

    tag_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=False
    )

    def __init__(self, product_id, tag_id):
        self.product_id = product_id
        self.tag_id = tag_id

    def __resp__(self):
        return f'<ProductTags {self.tag_id} for {self.product_id}>'