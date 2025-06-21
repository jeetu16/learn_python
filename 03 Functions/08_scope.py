message = 'a'


def greet(name):    # name is local parameter variable which scope will be within function
    global message  # bad practice to update global variable within a function.
    message = 'Hi'  # same applies for message variable


# print(name)
print(message)
