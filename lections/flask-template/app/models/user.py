from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from flask_login import UserMixin, AnonymousUserMixin
from app import db
from app.models.utils import ModelMixin
from app.utils import generate_password_reset_id


class User(db.Model, ModelMixin, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    reset_password_uuid = db.Column(db.String(64), default=generate_password_reset_id)

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @classmethod
    def authenticate(cls, user_identifier, password):
        user = cls.query.filter(
            db.or_(
                func.lower(cls.username) == func.lower(user_identifier),
                func.lower(cls.email) == func.lower(user_identifier),
            )
        ).first()
        if user is not None and check_password_hash(user.password, password):
            return user

    def reset_password(self):
        reset_uuid = generate_password_reset_id()
        self.password = reset_uuid
        self.reset_password_uuid = reset_uuid
        self.save()


class AnonymousUser(AnonymousUserMixin):
    pass
