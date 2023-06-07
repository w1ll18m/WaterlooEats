from database import main

class Resteraunt(main.db.Model):
    resteraunt_id = main.db.Column(
        main.db.Integer,
        primary_key=True
    )

    resteraunt_name = main.db.Column(
        main.db.String(256),
        unique=True,
        nullable=False
    )

    price_point = main.db.Column(
        main.db.String(128),
        unique=False,
        nullable=False
    )

    description = main.db.Column(
        main.db.Text,
        unique=False,
        nullable=True
    )

    products = main.db.relationship('Product', backref='resteraunt')

