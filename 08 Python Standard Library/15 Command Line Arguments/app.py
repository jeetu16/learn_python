import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python2 app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
