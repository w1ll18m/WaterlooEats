from ..extensions import db

class Resteraunt(db.Model):
    resteraunt_id = db.Column(
        db.Integer,
        primary_key = True
    )

    resteraunt_name = db.Column(
        db.String(512),
        unique=True,
        nullable=False
    )

    cuisine_type = db.Column(
        db.String(128),
        unique=False,
        nullable=False
    )

    location = db.Column(
        db.String(512),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.Text,
        unique=False,
        nullable=True
    )

    image_url = db.Column(
        db.Text,
        unique=False,
        nullable=False
    )

    delivery_fee = db.Column(
        db.Float,
        unique=False,
        nullable=False
    )

    products = db.relationship(
        "Product", 
        backref="resteraunt", 
        cascade="all, delete"
    )

    tags = db.relationship("Tag", backref="resteraunt", cascade="all, delete")

    hour = db.relationship("Hour", backref="resteraunt", cascade="all, delete", uselist=False)

    def __init__(self, resteraunt_name, cuisine_type, location, description, image_url, delivery_fee):
        self.resteraunt_name = resteraunt_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.description = description
        self.image_url = image_url
        self.delivery_fee = delivery_fee

    def __repr__(self):
        return f'<Resteraunt {self.resteraunt_name}>'

    