def saveUser(**user):
    for key in user:
        print(key, user[key])


saveUser(id=1, name="jeetu", age=28)
