def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


product = multiply(1, 4, 5, 3)
print(product)
