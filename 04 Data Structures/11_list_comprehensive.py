items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 15)
]

# replacement of map function
prices = [item[1]+1 for item in items]
print(prices)
# replacement of filter function
prices = [item for item in items if item[1] >= 10]
print(prices)
