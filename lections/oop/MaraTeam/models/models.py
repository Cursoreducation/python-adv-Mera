import json

class Plant:
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file, "r")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_plants(cls):
        data = cls.get_data()
        for plant in data:
            print(plant["name"])
            print(plant["location"])

    @classmethod
    def get_by_id(cls, id):
        plants = cls.get_data()
        counter = 0
        for plant in plants:
            if id == plant["id"]:
                print(plant["name"])
                print(plant["location"])
                break
            counter+=1
            if counter == len(plants):
                print("Not found plant with this id")

            
    
    def save(self):
        data = self.get_data()
        new_plant = {"name": self.name, "location": self.location}
        if len(data) > 0:
            new_plant["id"] = data[-1]["id"] + 1
        else:
            new_plant["id"] = 1
        data.append(new_plant)
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)




class Employee:
    file = "employees.json"

    def __init__(self, name, plant_id):
        self.name = name
        self.plant_id = plant_id
    
    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file, "r")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_employees(cls):
        data = cls.get_data()
        for employee in data:
            print(employee["name"])
            print(employee["plant_id"])

    @classmethod
    def get_by_id(cls, id):
        employees = cls.get_data()
        counter = 0
        for employee in employees:
            if id == employee["id"]:
                print(employee["name"])
                print(employee["plant_id"])
                break
            counter+=1
            if counter == len(employees):
                print("Not found plant with this id")

            
    
    def save(self):
        data = self.get_data()
        new_employee = {"name": self.name, "plant_id": self.plant_id}
        if len(data) > 0:
            new_employee["id"] = data[-1]["id"] + 1
        else:
            new_employee["id"] = 1
        data.append(new_employee)
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)