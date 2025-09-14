_pizzaList = ["Cheese Pizza", "Pepperoni Pizza", "Stuffed Crust Pizza"]  # Time to comply with PEP-8.

for pizzas in _pizzaList:
    print(f"I like {pizzas}")

print("\nI really do like pizza!")
print("They can contain many types of ingredients.")
print("Is also very good.")
print("I do like pepperoni, cheese, chicken pizzas as its my usual.")

friendPizzas = _pizzaList[:]
_pizzaList.append("Meat Lovers Pizza")
friendPizzas.append("Pinapple on Pizza")

print(f"\nMy favorite pizzas are")
for pizza in _pizzaList:
    print(pizza)

print(f"\nMy friend's pizzas are")
for pizza in friendPizzas:
    print(pizza)
