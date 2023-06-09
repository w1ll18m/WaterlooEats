from .. import db

class Product(db.Model):
    product_id = db.Column(
        db.Integer,
        primary_key=True
    )

    product_name = db.Column(
        db.String(128),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.Text,
        unique=False,
        nullable=True
    )

    price = db.Column(
        db.Float,
        unique=False,
        nullable=False
    )

    calorie_count = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )

    image_url = db.Column(
        db.Text,
        unique=False,
        nullable=True
    )

    resteraunt_id = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )

    def __init__(self, product_name, description, price, calorie_count, image_url, resteraunt_id):
        self.product_name = product_name
        self.description = description
        self.price = price
        self.calorie_count = calorie_count
        self.image_url = image_url
        self.resteraunt_id = resteraunt_id

    def __repr__(self):
        return f'<Product {self.name}>'