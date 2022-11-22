from app import db
from app.models.utils import ModelMixin


class Recipient(db.Model, ModelMixin):

    __tablename__ = "recipients"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(16), nullable=True, unique=True)
    address = db.Column(db.String(255), nullable=True)
    birthday = db.Column(db.DateTime())

    active = db.Column(db.Boolean, default=True)
