candyList = {}
uniqueCandyList = []
finished = False
# chapter 6 (3.0) version, now with dictionaries.
# program will store multiple candies (or anything) per person.
while not finished:
    userInputName = input('What is your name?\n').title()  # everything is .title()d, spelling is important
    if userInputName in candyList:
        print("WARNING: It appears you've already added your candy. If you continue, you will overwrite your candy.")
    tempCandyList = []
    while True:  # loop for multiple candies per person
        userInputCandy = input('Type what candy you like? If you are finished, please type "done"\n').title()
        if (userInputCandy.lower()) == "done":
            print(f"Thank you {userInputName} for adding your candies.")
            break
        else:
            tempCandyList.append(userInputCandy)
            print(f"Added {userInputCandy} to {userInputName} to the list.")
            uniqueCandyList.append(userInputCandy)
    if len(tempCandyList) > 0:
        candyList.update({userInputName: tempCandyList})  # the only dictionary used
    while True:  # loop to add multiple people
        completion = input("Is there more people to add? y/n\n").lower()
        if completion == "y" or completion == "yes":
            break
        elif completion == "n" or completion == "no":
            finished = True  # will stop the whole while loop
            break

print(f"\nDictionary here v\n{candyList}")

print("\nDone? The favorite candy for each person are:")

last_candy = ["Candy Corn", "Kit Kat", "Gummy Bears", "Milky Way"]  # example list from last chapter 5

all_candy = []  # List for storing all the candies.

for key0, candies in candyList.items():  # Count every favorite candy.
    print(f"\n{key0}'s favorite candies are:")
    for candy in candies:
        print(f"{candy}")  # I am no longer picking the most popular candy.
        all_candy.append(candy)

for candy in all_candy:
    if candy not in last_candy:  # checks if candy is not in list
        last_candy.append(candy)  # adds to the list
