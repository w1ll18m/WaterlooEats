from ..extensions import db

class ProductTags(db.Model): # JointTable between Product and Tag
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.product_id"),
        primary_key=True,
        autoincrement=False
    )

    tag_id = db.Column(
        db.Integer,
        db.ForeignKey("tag.tag_id"),
        primary_key=True,
        autoincrement=False
    )

    def __init__(self, product_id, tag_id):
        self.product_id = product_id
        self.tag_id = tag_id

    def __resp__(self):
        return f'<ProductTags {self.tag_id} for {self.product_id}>'