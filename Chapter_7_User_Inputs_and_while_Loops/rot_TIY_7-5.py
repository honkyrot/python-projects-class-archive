while True:
    ageInput = int(input("Please enter your age: "))
    if ageInput < 3:
        print("Your ticket will be free.")
    elif ageInput < 12:
        print("Your ticket will cost $10.")
    elif ageInput >= 12:
        print("Your ticket will cost $15.")
