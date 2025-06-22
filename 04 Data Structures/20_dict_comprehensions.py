values = []
for x in range(5):
    values.append(x*2)
print(values)

# doing above thing using map function
values = list(map(lambda item: item*2, range(5)))
print(values)

# doing above thing using list comprehensive
values = [item*2 for item in range(5)]
print(values)

# creating set using set comprehensive
values = {item*2 for item in range(5)}
print(values)

values = {}
for key in range(5):
    values[key] = key*2
print(values)

# doing above thing using dictonary comprehensive
values = {x: x*2 for x in range(5)}
print(values)
