# #7-1. Rental Car.
# car_type = input("What kind of rental car do you want: ")
# print(f"Let me see if I can find a {car_type}")

#7-2. Restaurant Seating
dinner_group = int(input("How many people are dining? "))
if dinner_group > 8:
    print("You'll have to wait for a table")
else:
    print(f"Your table is ready for {dinner_group} people")