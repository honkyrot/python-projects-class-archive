userNameDatabase = ["admin", "hong", "ibrahim", "chase", "gabriel"]
newUsers = ["blake", "elijah", "ethan", "nicholas", "hong"]

for Users in newUsers:
    findUser = userNameDatabase.count(Users.lower())
    if findUser > 0:
        print(f"Username \"{Users}\" is already taken, please choose a different username.")
    else:
        print(f"Username \"{Users}\" is available.")
