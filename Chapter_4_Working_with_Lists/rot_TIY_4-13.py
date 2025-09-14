restrauntFoods = ("noodle", "rice", "chicken", "cheese", "cake")
print(f"the restraunt currently serves: ")
for food in restrauntFoods:
    print(food)

# food[1] = "fried rice"  # This attempts to change the tuple, yet causes an error. Python will reject this.
print(f"the restraunt now serves: ")
restrauntFoods = ("noodle", "rice", "chicken", "sushi", "ice cream")  # New foods!
for food in restrauntFoods:
    print(food)
