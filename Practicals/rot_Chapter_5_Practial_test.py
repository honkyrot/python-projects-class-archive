candyList = []
uniqueCandyList = []
finished = False
# chapter 5 version, ive changed nothing important
# program will store multiple candies (or anything) per person.
while not finished:  # programing Python is so much easier when you already learned a language
    userInputName = input('What is your name?\n')  # everything is .title()d, spelling is important
    userInputName = userInputName.title()
    tempCandyList = []
    while True:  # loop for multiple candies per person
        userInputCandy = input('Type what candy you like? If you are finished, please type "done"\n')
        if (userInputCandy.lower()) == "done":
            print(f"Thank you {userInputName} for adding your candies.")
            break
        else:
            userInputCandy = userInputCandy.title()  # automatic spell case check, typos are not checked.
            tempCandyList.append(userInputCandy)
            print(f"Added {userInputCandy} to {userInputName} to the list.")
            uniqueCandyList.append(userInputCandy)
    candyList.append([userInputName, tempCandyList])
    while True:  # loop to add multiple people
        completion = input("Is there more people to add? y/n\n")
        completion = completion.lower()
        if completion == "y" or completion == "yes":
            break
        elif completion == "n" or completion == "no":
            finished = True  # will stop the whole while loop
            break

print("\nDone? The favorite candy for each person are:")

for names, candies in candyList:  # count every favorite candy.
    print(f"\n{names}'s favorite candies are:")
    for candy in candies:
        print(f"{candy}")

uniqueCandyList.sort()

popularCandy = ["candy", 0]  # example, value is discarded after one use

for candy in uniqueCandyList:  # count the candy popularity, alphabetical order takes precedence.
    number = uniqueCandyList.count(candy)
    if number > popularCandy[1]:
        popularCandy = [candy, number]

print(f"\nThe most popular candy is \n{popularCandy[0]} with {popularCandy[1]} likes!")
