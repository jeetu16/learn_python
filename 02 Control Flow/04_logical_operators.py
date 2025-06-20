highIncome = True
goodCredit = False
student = True

# and Operator
if highIncome and goodCredit:
    print("You are eligible for loan.")
else:
    print("You are not eligible for loan.")


# or Operator : It check if one of the condition True then it gives True as expression value.
if highIncome or goodCredit:
    print("You are eligible for loan.")
else:
    print("You are not eligible for loan.")

# not Operator
if not student:
    print('You can not join the University Workshop.')
else:
    print('You can join the University Workshop.')

# compound condition:
if (highIncome or goodCredit) and not student:
    print("You are eligible for loan.")
else:
    print("You are not eligible for loan.")
