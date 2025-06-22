# Set : Set is another data structure which is a collection with no duplicate values. It is unordered sequence of list.
numbers = {1, 2, 3, 4, 5, 5, 2}
numbers2 = set(numbers)
print(numbers)
print(numbers2)
numbers.add(9)
numbers.remove(1)
print(len(numbers))
print(numbers)

# Math operations

first = {1, 2, 3, 4}
second = {1, 5}

# Union of sets - Take all the ditinct items from both the sets
print(first | second)

# Intersection of sets - Take common items from both the sets
print(first & second)

# difference between two sets - Take all the items from first sets which second set don't have
print(first - second)

# symetric difference - It return items either first or second set but not both.
print(first ^ second)

# we check existence of item in set using in operator

print(7 in second)
