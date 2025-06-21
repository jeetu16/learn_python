# Two types of function we create.
# 1 - Perform a task
# 2 - Return a value

def greet(name):
    print(f"Hi {name}")


def getGreeting(name):
    return f"Hi {name}"


greet("Jeetu")
message = getGreeting("Hemant")
file = open('context.txt', 'w')
file.write(message)
