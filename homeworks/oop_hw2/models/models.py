import json


class Toyota:
    file = "toyota.json"

    def __init__(self, drive, gear, color):
        self.drive = drive
        self.gear = gear
        self.color = color

    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file, "r")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_toyotas(cls):
        data = cls.get_data()
        for toyota in data:
            print(toyota)
            # print(toyota["gear"])
            # print(toyota["color"])

    @classmethod
    def get_by_id(cls, id: object) -> object:
        toyotas = cls.get_data()
        counter = 0
        for toyota in toyotas:
            if id == toyota["id"]:
                print(toyota["drive"])
                print(toyota["gear"])
                print(toyota["color"])
                break
            counter += 1
            if counter == len(toyotas):
                print("Not found toyota with this id")


    @classmethod
    def change_color_by_id(cls, id: object) -> object:
        toyotas = cls.get_data()
        counter = 0
        for toyota in toyotas:
            if id == toyota["id"]:
                new_color = input("Input new color: ")
                toyota["color"] = new_color
                # print(toyota["color"])
                # for x in toyotas:
                #     print(x)
                file = open("database/" + cls.file, "w")
                data_in_json = json.dumps(toyotas)
                file.write(data_in_json)
                break
            counter += 1
            if counter == len(toyotas):
                print("Not found toyota with this id")


    @classmethod
    def change_gear_by_id(cls, id: object) -> object:
        toyotas = cls.get_data()
        counter = 0
        for toyota in toyotas:
            if id == toyota["id"]:
                new_gear = input("Input gear: ")
                toyota["gear"] = new_gear
                file = open("database/" + cls.file, "w")
                data_in_json = json.dumps(toyotas)
                file.write(data_in_json)
                break
            counter += 1
            if counter == len(toyotas):
                print("Not found toyota with this id")


    def save(self):
        data = self.get_data()
        new_toyota = {"drive": self.drive, "gear": self.gear, "color": self.color}
        if len(data) > 0:
            new_toyota["id"] = data[-1]["id"] + 1
        else:
            new_toyota["id"] = 1
        data.append(new_toyota)
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)



