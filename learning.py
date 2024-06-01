#7-8. Deli
# sandwich_orders = ["Turkey Sandwich","Ham Sandwich","Chicken Sandwich","Icecream Sandwich","Pastrami Sandwich","Pastrami Sandwich","Pastrami Sandwich"]
# finished_sandwiches = []

# # while sandwich_orders:
# #     finished_sandwich = sandwich_orders.pop()
# #     finished_sandwiches.append(finished_sandwich)

# #     print(f"Finished with {finished_sandwich}")

# # print(f"\nHere are your sandwiches:")
# # for each_sandwich in finished_sandwiches:
# #     print(f"\n{each_sandwich}")
    


# #7-9.No Pastrami
# lowered_sandwich_names = [lowered_each_sandwich.lower() for lowered_each_sandwich in sandwich_orders]
# while "pastrami sandwich" in lowered_sandwich_names:
#     lowered_sandwich_names.remove("pastrami sandwich")
# print(lowered_sandwich_names)

#7-10. Dream Vacation
dream_vacation = {}
poll = True
while poll:
    name = input("What is your name?")
    location = input("What is your dream location to visit?")

    dream_vacation[name] = location

    repeat = input("Would you like someone else to take the poll? (yes/no)")
    if repeat == "no":
        poll = False

print(f"Here are the results:\n")
for name,location in dream_vacation.items():
    print(f"{name.title()} wants to visit {location.title()}")