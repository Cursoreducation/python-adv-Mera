from homeworks.oop2_hw3.models.models import Plant, Employee, Salon

while True:
    print("1. Add new Plant\n" +
          "2. Get all plants\n" +
          "3. Get Plant by Id\n" +
          "4. Add new Employee\n" +
          "5. Get all employees\n" +
          "6. Get Employee by Id\n" +
          "7. Add new Salon\n" +
          "8. Get all salons\n" +
          "9. Get Salon by Id\n"
        )
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("PLant name: ")
        location = input("Plant location: ")
        plant = Plant(name, location)
        plant.save()
    elif flag == 2:
        Plant.get_all()
    elif flag == 3:
        id = int(input("Type id to search: "))
        plant = Plant.get_by_id(id)
        Plant.print_object([plant])
    elif flag == 4:
        name = input("Employee name: ")
        object_id = input("Employee work id: ")
        type_of_work = input("Where work Employee?: ")
        employee = Employee(name, object_id, type_of_work)
        employee.save()
    elif flag == 5:
        Employee.get_all()
    elif flag == 6:
        id = int(input("Type id to search: "))
        Employee.get_by_id(id)
    elif flag == 7:
        name = input("Salon name: ")
        address = input("Address: ")
        size = input("Size: ")
        salon = Salon(name, address, size)
        salon.save()
    elif flag == 8:
        Salon.get_all()
    elif flag == 9:
        id = int(input("Type id to search: "))
        salon = Salon.get_by_id(id)
        Salon.print_object([salon])

