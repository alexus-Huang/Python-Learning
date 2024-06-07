class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        description = f"{self.make} {self.model} {self.year}"
        return description

    def fill_gas_tank(self):
        print("Filling up gas!")

class Battery:
    def __init__(self,battery_cap,battery_size=59):
        self.battery_size = battery_size
        self.battery_cap = battery_cap
    
    def battery_level(self):
        print(f"Battery: {self.battery_size}")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(2)




