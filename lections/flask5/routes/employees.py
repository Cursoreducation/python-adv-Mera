from app import app, db
from models.models import Employee, Plant
from flask import render_template, request, redirect


@app.route("/employees")
def employees_home():
    employees = Employee.query.all()
    return render_template("employees-list.html", employees=employees)


@app.route("/add-employee", methods=["POST", "GET"])
def add_employee():
    if request.method == "POST":
        data = request.form
        try:
            employee = Employee(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                email=data.get("email"),
                plant_id=int(data.get("plant_id"))
            )
            db.session.add(employee)
            db.session.commit()
        except:
            return "This email already exist!"
        return redirect("/employees")
    else:
        plants = Plant.query.all()
        return render_template("add-employee.html", plants=plants)

