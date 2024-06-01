#7-8. Deli
sandwich_orders = ["Turkey Sandwich","Ham Sandwich","Chicken Sandwich","Icecream Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)

    print(f"Finished with {finished_sandwich}")

print(f"\nHere are your sandwiches:")
for each_sandwich in finished_sandwiches:
    print(f"\n{each_sandwich}")
    


#7-9.No Pastrami