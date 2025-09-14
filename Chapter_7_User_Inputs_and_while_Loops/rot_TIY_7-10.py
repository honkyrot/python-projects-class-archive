locations = []
while True:
    user_name_vacation = input("Hey user!, what is your name? : ").title()
    user_vacation = input(f"Alright {user_name_vacation}, where would you like to go for a vacation? : ").title()
    print(f"Thank you for adding your location, your data has been recorded.")
    locations.append(user_vacation)
    completion = input("Is that everyone? y/n\n").lower()
    if completion == "y" or completion == "yes":
        break
    elif completion == "n" or completion == "no":
        continue

print("\nPoll concluded, tallying results.\n")
print("People wish to go to these places: ")
for place in locations:
    print(place)
