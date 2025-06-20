# Solution 1:
# i = 0
# for num in range(2, 10, 2):
#     print(num)
#     i += 1

# print(f"We have {i} even numbers.")


# Solution 2:
count = 0
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
        count += 1
print(f"We have {count} even numbers.")
