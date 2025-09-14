# hello admin
userNameDatabase = ["Admin", "Hong", "Ibrahim", "Chase", "Gabriel"]
userNameSignIn = input("Please input your username.\n")

if userNameSignIn.title() in userNameDatabase:
    if userNameSignIn.title() == "Admin":
        print("Hello administrator, would you like to see a status report?")
    else:
        print(f"Hello {userNameSignIn.title()}, thank you for logging in again.")
else:
    print(f"Username not in database.")
