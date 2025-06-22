# Tuple : tuple is read only list. We can not modified sequence, can't add new items, can't remove existing items from tuples.

point = (1, 2, 3, 4)
point2 = 1, 2
point3 = 1,
point4 = 1  # Not a tuple.
point5 = ()
point6 = (1, 2) + (3, 4)
point7 = (1, 2) * 3
point8 = tuple([1, 2])
point9 = tuple("Hello World")
p, q, r, s = point


print(point[0])
print(point[0:2])
print(point)

if 10 in point:
    print("exists")

# point[0] = 39 # we can't modified tuple values. It will throw an error.

print(point)

print(point.count(2))
print(point.index(4))
