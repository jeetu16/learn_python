# there are times that we need to work with use external resources like files, network connection, databases etc. Whenever we use this resources after we are done we need to release them.
# For example, when we open a file. we should always close it after we are done otherwise another process or another program may not be able to access that file.
# To solve this problem inside the exception handling. we use finally.
try:
    file = open('app.py')
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
