from ..extensions import db

class ResterauntOwner(db.Model):
    id = db.Column(
        db.Integer,
        primary_key = True
    )

    public_id = db.Column(
        db.String(32),
        nullable = False,
        unique = True
    )

    username = db.Column(
        db.String(30),
        nullable = False,
        unique = True,
        index = True
    )

    password = db.Column(
        db.String(30),
        nullable = False,
        unique = False
    )

    email = db.Column(
        db.String(50),
        nullable = False,
        unique = True,
        index = True
    )

    created_at = db.Column(
        db.DateTime,
        unique = False,
        nullable = True
    )

    def __init__(self, public_id, username, password, email, created_at):
        self.public_id = public_id
        self.username = username
        self.password = password
        self.email = email
        self.created_at = created_at
    
    def __repr__(self):
        return f'<ResterauntOwner {self.username}>'