number = 100
command = ""

while number > 0:
    print(number)
    number //= 2

while command.lower() != "exit()":
    command = input(">>> ")
    print(command)
