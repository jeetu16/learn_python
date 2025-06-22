from sys import getsizeof
# Generator : Generator objects are iterable so just like list we can iterate over them and each iterations they genrate and speed out a new value.

values = (x*2 for x in range(100000))
print("gen: ", getsizeof(values))
# print(values[-1]) # TypeError: 'generator' object is not subscriptable

values = [x*2 for x in range(100000)]
print("list: ", getsizeof(values))
