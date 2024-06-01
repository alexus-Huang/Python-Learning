#7-8. Deli
sandwich_orders = ["Turkey Sandwich","Ham Sandwich","Chicken Sandwich","Icecream Sandwich","Pastrami Sandwich","Pastrami Sandwich","Pastrami Sandwich"]
finished_sandwiches = []

# while sandwich_orders:
#     finished_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(finished_sandwich)

#     print(f"Finished with {finished_sandwich}")

# print(f"\nHere are your sandwiches:")
# for each_sandwich in finished_sandwiches:
#     print(f"\n{each_sandwich}")
    


#7-9.No Pastrami
lowered_sandwich_names = [lowered_each_sandwich.lower() for lowered_each_sandwich in sandwich_orders]
while "pastrami sandwich" in lowered_sandwich_names:
    lowered_sandwich_names.remove("pastrami sandwich")
print(lowered_sandwich_names)