# #7-4. Pizza Toppings
# my_toppings_prompt = "Enter in your pizza toppings \n(Enter quit when you're done): "
# while True:
#     user_toppings = input(my_toppings_prompt)
#     if user_toppings == "quit":
#         break
#     else:
#         print(f"\nI'll add {user_toppings} to your pizza!")

#7-5. Movie Tickets
age_prompt = "Enter your age to find out your ticket price\n(Enter 'q' when you're done): "
under_three = 0
three_and_twelve = 10
over_twelve = 15
while True:
    user_age = input(age_prompt)
    if user_age == "q":
        break
    elif int(user_age) < 3:
        print(f"Your ticket price is ${under_three}")
    elif int(user_age) <=12:
        print(f"Your ticket price is ${three_and_twelve}")
    else:
        print(f"Your ticket price is ${over_twelve}")