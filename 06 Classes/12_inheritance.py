class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def eat(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)
