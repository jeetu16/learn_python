import random
import string

print(random.random())
print(random.randint(1, 100))
print(random.choice([1, 2, 3, 4, 5, 6]))
print(random.choices([1, 2, 3, 4, 5, 6], k=2))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

print(string.ascii_letters)
print(string.digits)

numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
print(numbers)
