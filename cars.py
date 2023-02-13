class Car:
       """A simple attempt to represent a car."""

       def __init__(self, make, model, year):
           self.make = make
           self.model = model
           self.year = year
           self.odometer_reading = 0

       def get_descriptive_name(self):
           long_name = f"{self.year} {self.make} {self.model}"
           return long_name.title()
       
       def fill_gas_tank(self):
           print(f"Glug glug glug, {self.make}'s tank has been filled.")

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

    def __init__(self, battery_size=75):
           """Initialize the battery's attributes."""
           self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def miles_per_battery(self):
        bat = self.battery_size
        if self.battery_size <=75:
            print(f"A car with a {bat}-kWh battery can go for ~ 300 miles.")
        else:
            print(f"A car with a {bat}-kWh battery can go for more than 300 miles.")

    def update_battery(self, newbatt):
        self.battery_size += newbatt
        self.password = "ichrzagt5ichrzagt2"

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")


def car_desc():
    car=input("What is your car name? ")
    if car == "Tesla":
        print(my_tesla.get_descriptive_name())
        print(my_tesla.read_odometer())
        print(my_tesla.fill_gas_tank())   

my_ford = Car('Ford','EcoSport', 2012)

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_prius = ElectricCar('prius', 'model chups', 2022)

print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(500)
my_tesla.increment_odometer(500)

my_tesla.read_odometer()
my_tesla.fill_gas_tank()
my_ford.fill_gas_tank()

my_tesla.battery.update_battery(85)
my_tesla.battery.describe_battery()
my_tesla.battery.miles_per_battery()
my_prius.battery.describe_battery()
my_prius.battery.miles_per_battery()


