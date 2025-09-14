candyList = []
finished = False

while not finished:  # yes I know it's a while loop, don't mind it. I find it much faster than copying same lines over.
    userInput = input(f'Type what candy you like, when you are done, please type "done"\n')
    if (userInput.lower()) == "done":
        finished = True
    else:  # else!
        candyList.append(userInput.title())
        print(f"Added {userInput.title()} to the list.")
print(f"\nDone? The favorite candy are\n")

for candy in candyList:  # eat the candy
    print(candy)
