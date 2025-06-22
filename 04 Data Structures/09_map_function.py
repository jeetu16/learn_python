items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 15)
]

# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)

# map function return map which is another iterable. so we can covert map into list
prices = list(map(lambda item: item[1], items))
print(prices)
