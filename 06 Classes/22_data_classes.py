from collections import namedtuple
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)
# print(id(p1))
# print(id(p2))
Point = namedtuple("Point", ['x', 'y'])
p1 = Point(x=1, y=2)
# it will throw an error because we can't change the value of variable. If we want to change the value then we have to re-assign the values.
p1.x = 10
p2 = Point(1, 2)
print(p1 == p2)
