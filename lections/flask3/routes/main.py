from app import app
from flask import render_template
from models.models import Plant


@app.route("/")
def main():
    plants = Plant.query.order_by(Plant.title.asc()).all()
    print(plants)
    return render_template("index.html", plants=plants)