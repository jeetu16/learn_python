# When writing programs many things can go wrong. Our program encounter an error and terminate. Usually this errors happens because of programmer mistakes or bad data that we get from the user or resources not being available.
# For example, you might need to open a file but if that file doesn't exists our file is going to crash. It's your job as programmer to prevent your application from crashing in this kind of situations.

# Example 1
numbers = [1, 2]
print(numbers[3])
# Error :
# IndexError: list index out of range

# Example 2
# If here we enter non-numeric value our program crashed
age = int(input("Age: "))
# Error:
# ValueError: invalid literal for int() with base 10: 'a'
