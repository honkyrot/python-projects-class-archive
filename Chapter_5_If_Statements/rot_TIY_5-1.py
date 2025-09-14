costOfPizza = 9.99
moneyInHand = 40.00
moneyInBank = 200.00

print(f"Do I have enough money for one pizza? I should have more than enough.")
print(moneyInHand >= costOfPizza)  # true

print(f"\nDo I have enough money for 3 pizzas? I should have enough.")
print(moneyInHand >= costOfPizza * 3)  # true

print(f"\nDo I have enough money for 6 pizzas? I don't have enough.")
print(moneyInHand >= costOfPizza * 6)  # false

print(f"\nCan I deposit $50 to my account? Probably not.")
print(moneyInHand >= 50)  # false

print(f"\nHow about depositing $30 to my account? Probably can.")
print(moneyInHand >= 30)  # true

print(f"\nHow about withdrawing $200 to my account? Probably can.")
print(moneyInBank >= 200)  # true

print(f"\nWill depositing $40 to my account make it 240 or more? Probably.")
print(moneyInBank + moneyInBank >= 240)  # true

print(f"\nCan I withdraw 250 from my account? Probably not.")
print(moneyInBank >= 250)  # false

print(f"\nCan I buy 100 pizzas?.")
print(moneyInHand >= costOfPizza * 100)  # false

print(f"\n What if I withdraw to buy 100 pizzas?.")
print(moneyInHand + moneyInBank >= costOfPizza * 100)  # false
