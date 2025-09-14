# Numbers Served

class Restaurant:
    def __init__(self, name, food_type):
        self.restaurant_name = name
        self.cuisine_type = food_type
        self.food_served = 0

    def set_number_served(self, set_num):
        self.food_served = set_num

    def increment_served(self, inc_num):
        self.food_served += inc_num

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The restaurant currently serves {self.cuisine_type}")

    def get_served(self):
        return f"The restaurant has served {self.food_served} people!"

    @staticmethod
    def open_restaurant():
        print("The restaurant is now open!")


class IceCreamRestaurant(Restaurant):
    def __init__(self, name, food_type, flavors):
        super(IceCreamRestaurant, self).__init__(name, food_type)
        self.flavors = flavors

    def describe_flavors(self):
        return f"The ice cream flavors are: " + ", ".join(self.flavors)


restaurant = Restaurant("Burger King", "Burgers")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.get_served())  # should day 0
restaurant.set_number_served(100)  # set to 100
print()  # break

icecream_stand = IceCreamRestaurant("Dairy Queen", "Ice Cream", ["Chocolate", "Vanilla", "Strawberry"])
icecream_stand.describe_restaurant()
print(icecream_stand.describe_flavors())
icecream_stand.open_restaurant()
