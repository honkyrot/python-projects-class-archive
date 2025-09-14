class Restaurant:
    def __init__(self, name, food_type):
        self.restaurant_name = name
        self.cuisine_type = food_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The restaurant currently serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")


restaurant1 = Restaurant("Burger King", "Burgers")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print()
restaurant2 = Restaurant("Dairy Queen", "Ice Cream")
restaurant2.describe_restaurant()
print()
restaurant3 = Restaurant("KFC", "Chicken")
restaurant3.describe_restaurant()
