numbers = [1, 2, 3, 4]
# unpacking operator. it is simmilar like spread operator of javascript.
print(*numbers)

# Useful application of unpacking operator
# We can use unpacking operator with any iterables

# 1. For creating list
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

# 2. for combining the list
first = [1, 2, 3, 4]
second = [4, 5, 6]
values = [*first, *second]
print(values)

# 3. We can use this with dictonary as well
first = {"x": 1}
second = {"x": 10, "y": 20}
combined = {**first, **second, "z": 30}
print(combined)
