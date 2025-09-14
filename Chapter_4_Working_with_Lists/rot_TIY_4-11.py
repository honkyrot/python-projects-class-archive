pizzaList = ["Cheese Pizza", "Pepperoni Pizza", "Stuffed Crust Pizza"]

for pizzas in  pizzaList:
    print(f"I like {pizzas}")

print("\nI really do like pizza!")
print("They can contain many types of ingredients.")
print("Is also very good.")
print("I do like pepperoni, cheese, chicken pizzas as its my usual.")

friendPizzas = pizzaList[:]  # :copy() is an option too.
pizzaList.append("Meat Lovers Pizza")  # append to first list
friendPizzas.append("Pinapple on Pizza")  # append to copied list

print(f"\nMy favorite pizzas are:")
for pizza in pizzaList:
    print(pizza)

print(f"\nMy friend's pizzas are")
for pizza in friendPizzas:
    print(pizza)
