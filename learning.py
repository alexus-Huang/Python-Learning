# #7-4. Pizza Toppings
# my_toppings_prompt = "Enter in your pizza toppings \n(Enter quit when you're done): "
# while True:
#     user_toppings = input(my_toppings_prompt)
#     if user_toppings == "quit":
#         break
#     else:
#         print(f"\nI'll add {user_toppings} to your pizza!")

#7-5. Movie Tickets
# age_prompt = "Enter your age to find out your ticket price\n(Enter 'q' when you're done): "
# under_three = 0
# three_and_twelve = 10
# over_twelve = 15
# while True:
#     user_age = input(age_prompt)
#     if user_age == "q":
#         break
#     elif int(user_age) < 3:
#         print(f"Your ticket price is ${under_three}")
#     elif int(user_age) <=12:
#         print(f"Your ticket price is ${three_and_twelve}")
#     else:
#         print(f"Your ticket price is ${over_twelve}")


#7-6. Three Exits
# Verson 1 - Use a conditional test in a while statement to stop the loop
# my_toppings_prompt = "Enter in your pizza toppings \n(Enter quit when you're done): "
# while True:
#     user_toppings = input(my_toppings_prompt)
#     if user_toppings == "quit":
#         break
#     else:
#         print(f"\nI'll add {user_toppings} to your pizza!")

        
# # Verson 2 - Use an active variable to control how long the loop runs  + V3 - Use a break statement to exit the loop when the user enters a 'quit' value
# my_toppings_prompt = "Enter in your pizza toppings \n(Enter quit when you're done): "
# active = True
# while active:
#     user_toppings = input(my_toppings_prompt)
#     if user_toppings == "quit":
#         active = False
#     else:
#         print(f"\nI'll add {user_toppings} to your pizza!")


#7-7. Infinity
while True:
    print(1)