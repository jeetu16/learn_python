age = 18

eligible = "You are eligible for voting"
notEligible = "You are not eligible for voting"

message = eligible if age >= 18 else notEligible
print(message)
