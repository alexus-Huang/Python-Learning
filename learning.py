#7-4. Pizza Toppings
my_toppings_prompt = "Enter in your pizza toppings \n(Enter quit when you're done): "
while True:
    user_toppings = input(my_toppings_prompt)
    if user_toppings == "quit":
        break
    else:
        print(f"\nI'll add {user_toppings} to your pizza!")