class Restaurant:
    def __init__(self, name, food_type):
        self.restaurant_name = name
        self.cuisine_type = food_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The restaurant currently serves {self.cuisine_type}")

    @staticmethod
    def open_restaurant():
        print("The restaurant is now open!")


restaurant = Restaurant("Burger King", "Burgers")
restaurant.describe_restaurant()
restaurant.open_restaurant()
