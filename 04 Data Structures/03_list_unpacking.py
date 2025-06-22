numbers = [1, 2, 3, 4, 5]
# list unpacking
a, b, *other = numbers
first, *middle, last = numbers
print(a, b, other)
print(first, middle, last)
