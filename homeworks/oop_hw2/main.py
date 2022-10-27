# from operator import iadd
from models.models import Toyota

while True:
    print("0. Exit\n" +
          "1. Add new Toyota\n" +
          "2. Get all toyotas\n" +
          "3. Get Toyota by Id\n" +
          "4. Change color by Id\n" +
          "5. Change gear by ID"
          )
    flag = int(input("Choose menu item: "))
    if flag == 0:
        exit()
    elif flag == 1:
        drive = input("Toyota's drive type (FWD, RWD, AWD, 4WD): ")
        gear = input("Input gear type (auto, manual): ")
        color = input("Input color: ")
        toyota = Toyota(drive, gear, color)
        toyota.save()
    elif flag == 2:
        Toyota.get_all_toyotas()
    elif flag == 3:
        id = int(input("Type id to search: "))
        Toyota.get_by_id(id)
    elif flag == 4:
        id = int(input("Type id to change color: "))
        Toyota.change_color_by_id(id)
    elif flag == 5:
        id = int(input("Type id to change gear: "))
        Toyota.change_gear_by_id(id)

