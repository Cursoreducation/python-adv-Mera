from app import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    employees = db.relationship("Employee", back_populates="plant")


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    plant_id = db.Column(db.Integer, db.ForeignKey("plant.id"), nullable=False)
    plant = db.relationship("Plant", back_populates="employees")