from ..extensions import db

class Hour(db.Model):
    hours_id = db.Column(
        db.Integer,
        primary_key=True
    )

    resteraunt_id = db.Column(
        db.Integer,
        db.ForeignKey("resteraunt.resteraunt_id"),
        unique=True,
        nullable=False
    )

    opening_hours = db.Column(
        db.Text,
        unique=False,
        nullable=False
    )

    closing_hours = db.Column(
        db.Text,
        unique=False,
        nullable=False
    )

    def __init__(self, resteraunt_id, opening_hours, closing_hours):
        self.resteraunt_id = resteraunt_id
        self.opening_hours = opening_hours
        self.closing_hours = closing_hours

    def __repr__(self):
        return f'<Opening {self.opening_hours} and Closing {self.closing_hours}>'