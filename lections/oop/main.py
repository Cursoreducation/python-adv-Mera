class Animal:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def run(self):
        print("running")

    def sound(self):
        print("sound")


class Dog(Animal):
    def sound(self):
        print("woof")
    
    def jump(self):
        print("Jump")


class Cat(Animal):
    def sound(self):
        print("meow")

    def eat(self):
        print("Eat")


animal1 = Animal("browko")
animal1.say_name()
animal1.sound()
dog = Dog("Uran")
dog.say_name()
dog.sound()
dog.jump()
cat = Cat("Nuska")
cat.say_name()
cat.sound()
cat.eat()