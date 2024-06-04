#8-12. Sandwiches
def build_sandwich(*toppings):
    print(f"Here is what you want on your toppings")
    for each_topping in toppings:
        print(f"- {each_topping}")

build_sandwich("cheese","lettuce","tomatoes")