# Stack : stack works on LIFO behavior(Last In First Out)
browsingSession = []
browsingSession.append(1)
browsingSession.append(2)
browsingSession.append(3)

print(browsingSession)

last = browsingSession.pop()
print(last)
print(browsingSession)

print(browsingSession[-1])

if not browsingSession:
    print("disable back button")
