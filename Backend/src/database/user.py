from .. import db

class User(db.Model):
    id = db.Column(
        db.String(256),
        primary_key = True
    )

    email = db.Column(
        db.String(50),
        nullable = False,
        unique = True
    )

    phone_number = db.Column(
        db.String(10),
        nullable = False,
        unique = True
    )

    address = db.Column(
        db.String(128),
        nullable = False,
        unique = False
    )

    def __init__(self, id, email, phone_number, address):
        self.id = id
        self.email = email
        self.phone_number = phone_number
        self.address = address
    
    def __repr__(self):
        return f'<User {self.id}>'