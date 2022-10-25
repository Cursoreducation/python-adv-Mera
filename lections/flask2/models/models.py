from framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


    def _protected_example(self):
        return "protected"


    def __private_example(self):
        return "private"


class Employee(Model):
    file = "employees.json"

    def __init__(self, name, object_id, type_of_work):
        self.name = name
        self.object_id = object_id
        self.type_of_work = type_of_work

    def get_work(self):
        # Витягуєм данні про роботу
        if self.type_of_work == "plant":
            return Plant.get_by_id(self.object_id)
        elif self.type_of_work == "salon":
            return Salon.get_by_id(self.object_id)
        else:
            return {}

    @classmethod
    def get_by_id(cls, id):
        # Викликаєм батьківський метод get_by_id (get_by_id з класу Model)
        employee_dict = super().get_by_id(id)
        employee = Employee(employee_dict["name"], int(employee_dict["object_id"]), employee_dict["type_of_work"])
        work_of_employee = employee.get_work()
        cls.print_object([employee_dict])
        print("Employee work: ")
        cls.print_object([work_of_employee])


class Salon(Model):
    file = "salons.json"

    def __init__(self, name, address, size):
        self.name = name
        self.address = address
        self.size = size