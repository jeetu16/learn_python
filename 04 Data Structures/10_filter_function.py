items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 15),
    ("Product4", 11)
]

filtered = list(filter(lambda item: item[1] >= 10, items))
# for item in filtered:
#     print(item)
print(filtered)
print(type(filter(lambda item: item[1] >= 10, items)))
