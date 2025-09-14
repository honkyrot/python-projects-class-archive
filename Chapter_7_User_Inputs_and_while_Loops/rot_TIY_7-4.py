while True:
    topping = input(f"What kind of topping would you like on your pizza? If you're done, please type 'quit'.\n: ")
    if topping.lower() != "quit":
        print(f"Adding the topping {topping.title()} to the pizza!")
    else:
        print("Finished adding toppings.")
        break
