items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 15)
]

# lambda function syntac
# items.sort(key=lambda parameters: expression)
items.sort(key=lambda item: item[1])
print(items)
