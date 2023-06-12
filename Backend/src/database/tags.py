from .. import db

class Tag(db.Model): # One-to-Many relationship between Resteraunt and Tag
    tag_id = db.Column(
        db.Integer,
        primary_key=True
    )

    tag_name = db.Column(
        db.String(256),
        unique=True,
        nullable=False
    )

    resteraunt_id = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )

    def __init__(self, tag_name, resteraunt_id):
        self.tag_name = tag_name
        self.resteraunt_id = resteraunt_id

    def __repr__(self):
        return f'<Product {self.tag_name}>'