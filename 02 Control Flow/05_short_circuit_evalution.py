highIncome = True
goodCredit = False
student = True

# short circuit evalution
if highIncome and goodCredit and not student:
    print("You are eligible for loan.")
else:
    print("You are not eligible for loan.")
