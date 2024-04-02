toppings = []
if toppings:
    for every_topping in toppings:
        if every_topping =="cheese":
            print("No cheese at the moment")
        else:
            print(f"Adding {every_topping.title()}")
else:
    print("Do you really want a plain pizza?")