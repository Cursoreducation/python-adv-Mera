from app import app, db
from flask import render_template, request, redirect
from models.models import Plant, Employee


@app.route("/add-plant")
def add_plant():
    employees = Employee.query.all()
    return render_template("add_plant.html", employees=employees)


@app.route("/save-plant", methods=["POST"])
def save_plant():
    # print(request.form.getlist("employees"))
    name = request.form.get("name")
    location = request.form.get("location")
    plant = Plant(title=name, location=location)
    db.session.add(plant)
    for employee_id in request.form.getlist("employees"):
        employee = Employee.query.get(int(employee_id))
        employee.plant_id = plant.id
        db.session.add(employee)
    db.session.commit()
    return redirect("/")


@app.route("/delete-plant/<int:id>")
def delete_plant(id):
    plant = Plant.query.get(id)
    print(plant.id)
    db.session.delete(plant)
    db.session.commit()
    return redirect("/")


@app.route("/edit-plant/<int:id>")
def edit_plant(id):
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template("add_plant.html", plant=plant, employees=employees)


@app.route("/update-plant/<int:id>", methods=["POST"])
def update_plant(id):
    plant = Plant.query.get(id)
    plant.title = request.form.get("name")
    plant.location = request.form.get("location")
    db.session.add(plant)
    for employee_id in request.form.getlist("employees"):
        employee = Employee.query.get(int(employee_id))
        employee.plant_id = plant.id
        db.session.add(employee)
    db.session.commit()
    return redirect("/")