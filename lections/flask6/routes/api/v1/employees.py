from app import api, db
from flask_restful import Resource
from flask import request
from models.models import Employee as EmployeeModel


class EmployeesResource(Resource):
    def get(self):
        filter = request.args
        query = EmployeeModel.query
        if len(filter) < 1:
            employees = query.all()
        else:
            for key in filter.keys():
                print(key)
                employees = query.filter(getattr(EmployeeModel, key) == filter.get(key))

        employee_data = []
        for employee in employees:
            employee_data.append(employee.serialize())
        return employee_data


    def post(self):
        data = request.json
        employee = EmployeeModel(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            plant_id=int(data.get("plant_id"))
        )
        db.session.add(employee)
        db.session.commit()
        return employee.serialize()


class SingleEmployeeResource(Resource):
    def get(self, id):
        employee = EmployeeModel.query.get(id)
        return employee.serialize()

    def put(self, id):
        data = request.json
        employee = EmployeeModel.query.get(id)
        employee.first_name = data.get("first_name", employee.first_name)
        employee.last_name = data.get("last_name", employee.last_name)
        employee.email = data.get("email", employee.email)
        employee.plant_id = data.get("plant_id", employee.plant_id)
        db.session.add(employee)
        db.session.commit()
        return employee.serialize()


api.add_resource(EmployeesResource, "/api/v1/employees")
api.add_resource(SingleEmployeeResource, "/api/v1/employees/<int:id>")