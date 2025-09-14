sandwich_type = ["Chicken", "Egg", "Seafood", "Roast Beef", "BLT", "Grilled Cheese", "Ham",
                 "Nutella", "Grilled Chicken", "Meatball", "Ice Cream", "Prawn", "Olive",
                 "Oreo Ice Cream", "Salmon", "Tuna", "Vegetable", "Bread", "Cheese"]

finished_sandwiches = []

while sandwich_type:
    sandwich = sandwich_type.pop()
    finished_sandwiches.append(f"{sandwich} Sandwich")
    print(f"Making a {sandwich} Sandwich.")

print("\n Finished making all sandwiches!\n")

for sand in finished_sandwiches:
    print(f"Made a {sand} Sandwich.")

delivery_option = input("\nWould you like delivery for that? (y/n) : ").lower()
if delivery_option == "y" or delivery_option == "yes":
    print("Delivering the food now.")
elif delivery_option == "n" or delivery_option == "no":
    print("Please come pick up the food then.")
