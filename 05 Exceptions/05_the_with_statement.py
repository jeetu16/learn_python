# we use finally clause to release the external resourses. We have a shorter and clearn way to achieve the same thing but without the finally clause
# But it doesn't always work. It works with certain kind of objects.

try:
    # when we open a file with with statement it automatically call file.close() function we don't need to call that function.
    with open('app.py') as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
