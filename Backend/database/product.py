from database import main

class Product(main.db.Model):
    product_id = main.db.Column(
        main.db.Integer,
        primary_key=True
    )

    product_name = main.db.Column(
        main.db.String(128),
        unique=True,
        nullable=False
    )

    description = main.db.Column(
        main.db.Text,
        unique=False,
        nullable=True
    )

    price = main.db.Column(
        main.db.Float,
        unique=False,
        nullable=False
    )

    calorie_count = main.db.Column(
        main.db.Integer,
        unique=False,
        nullable=False
    )

    resteraunt_id = main.db.Column(
        main.db.Integer,
        main.db.ForeignKey("resteraunt.id")
    )

    def __init__(self, product_name, description, price, calorie_count):
        self.product_name = product_name
        self.description = description
        self.price = price
        self.calorie_count = calorie_count

    def __repr__(self):
        return f'<Product {self.name}>'