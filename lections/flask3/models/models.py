from app import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)