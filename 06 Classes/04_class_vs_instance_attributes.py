class Point:
    # This is class level attributes. This will be share for every instances of class and will be same for every instance of class.
    defaultColor = "red"

    def __init__(self, x, y):
        # These are instances level attributes. This will be different for every instance of class
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.defaultColor = "yellow"

point = Point(2, 3)
print(point.defaultColor)
print(Point.defaultColor)
point.draw()

another = Point(4, 5)
print(another.defaultColor)
another.draw()
