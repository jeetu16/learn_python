# Constructors : It is a special method inside a class that is called when we create a object of that class.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(2, 3)
print(point.draw())
