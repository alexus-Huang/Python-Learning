class Restaurant:
    def __init__(self,restaurant_name,cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        self.customers_served_alreaady = 0
    
    def restuarant_description(self):
        print(f"{self.restaurant_name.title()} has a(n) {self.cuisine} cuisine")
    
    def customers_served(self,served_customers):
        self.customers_served_alreaady += served_customers

my_restaurant = Restaurant("John's Restaurant","Asian")

my_restaurant.customers_served(1)
print(f"Customers served: {my_restaurant.customers_served_alreaady}")

my_restaurant.customers_served(1)
print(f"Customers served: {my_restaurant.customers_served_alreaady}")