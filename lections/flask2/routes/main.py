from app import app
from flask import render_template
from models.models import Plant


@app.route("/")
def main():
    plants = Plant.get_data()
    return render_template("index.html", plants=plants)