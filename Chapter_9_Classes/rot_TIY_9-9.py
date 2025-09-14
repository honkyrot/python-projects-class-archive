class Car:
    def __init__(self, make, model, year):
        self.odometer_reading = 0
        self.year = year
        self.make = make
        self.model = model

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        mile_range = "Unknown"
        if self.battery_size == 40:
            mile_range = 150
        elif self.battery_size == 65:
            mile_range = 225
        print(f"This car can go about {mile_range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size == 40:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()

    @staticmethod
    def fill_gas_tank():
        print("This car doesn't have a gas tank!")

    def describe_battery(self):
        print(f"This car has a {self.battery}-kWh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
print("\nUpgrading Battery...\n")
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
