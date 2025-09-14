topping_amount = 0
# TIY 7-4 MODIFIED FOR TIY 7-6
while topping_amount < 5:
    topping = input(f"What kind of topping would you like on your pizza? If you're done, please type 'quit'.\n: ")
    if topping.lower() != "quit":  # conditional check, quits if it meets the quit.
        print(f"Adding the topping {topping.title()} to the pizza!")
        topping_amount += 1
    else:
        print("Finished adding toppings.")
        break  # break statement
    if topping_amount == 5:
        print("\nMaximum amount of toppings added!")  # active variable
