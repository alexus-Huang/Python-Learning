#9-1. Restaurant
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}\nCusine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")



new_restaurant = Restaurant("John's restaurant","asian cuisine")
new_restaurant.describe_restaurant()
print(f"\nRestaurant name: {new_restaurant.restaurant_name}")
new_restaurant.open_restaurant()