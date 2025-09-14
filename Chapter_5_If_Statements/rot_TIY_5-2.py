costOfPizza = 9.99
moneyInHand = 40.00
moneyInBank = 200.00
pocket = "Phone"
phoneModel = "Pixel 5a"
pizzaToppings = ["cheese", "pepperoni", "chicken"]

# Tests for equality and inequality with string
print(f"Is my phone a google Pixel? It should be true.")
print(phoneModel == "Pixel 5a")  # true

print(f"\nIs it a Pixel 6? It should be false.")
print(phoneModel == "Pixel 6")  # false

# Tests using the lower() method
print(f"\nDo I have a phone in my pocket, I should have.")
print(pocket.lower() == "phone")  # true

print(f"\nDo I have my wallet in my pocket? Should be false.")
print(pocket.lower() == "wallet")  # false

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
print(f"\nCan I deposit more than $50? I can't")
print(moneyInHand > 50)  # false

print(f"\nCan I deposit more than $30? I can")
print(moneyInHand > 30)  # true

print(f"\nCan I withdraw at least $100? I can")
print(moneyInBank >= 100)  # true

print(f"\nCan I withdraw at least $300? I cannot")
print(moneyInBank >= 300)  # false

# Test using the "and" keyword and the "or" keyword.
print(f"\nDo I have more than $20 on hand while keeping it less than $100? Should be true")
print(moneyInHand > 20 and moneyInHand < 100)  # true

print(f"\nCan I buy 5 pizzas or 8 pizzas? Can't get either of these, false.")
print(moneyInHand > costOfPizza*5 or moneyInHand > costOfPizza*8)  # false

# Test whether an item is in a list.
print(f"\nIs there cheese on my pizza? Yes")
print("cheese" in pizzaToppings)  # true

print(f"\nIs there bacon on my pizza? No")
print("bacon" in pizzaToppings)  # false

# Test whether an item is NOT in a list, I use "not" as its simple.
print(f"\nIs there not chicken on my pizza? No")
print(not "chicken" in pizzaToppings)  # false

print(f"\nIs there not pineapple on my pizza? Yes")
print(not "pineapple" in pizzaToppings)  # true
