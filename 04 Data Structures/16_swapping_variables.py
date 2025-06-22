x = 10
y = 12
print("Before Swap: ", x, y)

# Solution 1:
# c = x
# x = y
# y = c

# Solution 2:
# x = x+y
# y = x-y
# x = x-y

# Solution 3:
# x = x ^ y
# y = x ^ y
# x = x ^ y

# Solution 4:
y, x = x, y
print("After Swap: ", x, y)
