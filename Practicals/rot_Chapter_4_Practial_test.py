candyList = []
uniqueCandyList = []
finished = False
# program will store multiple candies per person. this took way to long to whip out
while not finished:  # programing Python is so much easier when you already learned a language
    userInputName = input(f'What is your name?\n')  # everything is case-sensitive
    tempCandyList = []
    while True:
        userInputCandy = input(f'Type what candy you like? If you are finished, please type "done"\n')
        if (userInputCandy.lower()) == "done":
            print(f"Thank you {userInputName.title()} for adding your candies.")
            break
        else:  # else!
            tempCandyList.append(userInputCandy.title())
            print(f"Added {userInputCandy.title()} to {userInputName.title()} to the list.")
            uniqueCandyList.append(userInputCandy.title())
    candyList.append([userInputName.title(), tempCandyList])
    while True:
        completion = input(f"Is that everyone? y/n\n")
        if completion.lower() == "y" or completion.lower() == "yes":
            finished = True
            break
        elif completion.lower() == "n" or completion.lower() == "no":
            break

print(f"\nDone? The favorite candy for each person are:")

for names, candies in candyList:  # eat the candy while using 2D! lists.
    print(f"\n{names}'s favorite candies are:")
    for candy in candies:
        print(f"{candy}")

uniqueCandyList.sort()

popularCandy = ["candy", 0]

for candy in uniqueCandyList:  # count the candy popularity
    number = uniqueCandyList.count(candy)
    if number > popularCandy[1]:
        popularCandy = [candy, number]

print(f"\nThe most popular candy is \n{popularCandy[0]} with {popularCandy[1]} likes!")
