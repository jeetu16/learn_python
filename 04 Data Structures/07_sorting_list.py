numbers = [3, 51, 2, 8, 6, 10, 1]
# it will not modify original list. it just return sorted list.
print(sorted(numbers))
print(numbers)
# it will modify original list.
numbers.sort(reverse=True)
print(numbers)

# sorting the tupple of list
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 15)
]


def sortItem(item):
    return item[1]


items.sort(key=sortItem)
print(items)
