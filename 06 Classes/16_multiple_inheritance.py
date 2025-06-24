class Person:
    def greet(self):
        print("Person Greet")


class Employee:
    def greet(self):
        print("Employee Greet")


class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()

# Good Example of Multiple Inheritance


class Flyer:
    def fly(self):
        print("Flying")


class Swimmer:
    def swimming(self):
        print("Swimming")


class FlyingFish(Flyer, Swimmer):
    pass
