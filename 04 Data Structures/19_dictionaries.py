# Dictionary : It is a collection of key n value pair. We use it to map a key to a value.
# Real world example for it key phone booth.
# In python we can only use immutable types for key. But for value we can use anything.
point = {"x": 1, "y": 2}
point2 = dict(x=1, y=3)

print(point["x"])
point["x"] = 10
print(point)
point["z"] = 30
print(point)

# finding key value
if "x" in point:
    print(point["x"])

print(point.get('x'))

# Loop over dictionary Method 1:
for key in point:
    print(key, point[key])

# Loop over dictionary Method 2:
for key, value in point.items():
    print(key, value)

# del the item from dictionary
del point["x"]
print(point.pop('z'))
