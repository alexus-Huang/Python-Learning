# # Functions
# def add_three(input_var):
#     output_var=input_var+3
#     return output_var

# new_number = add_three(3)
# # print(new_number)

# # My own function
# def sayHello():
#     return "Hello"

# # print(sayHello())


# #-------------------------------
# # Using math.ceil()
# import math
# a_number=1.1
# rounded_value=math.ceil(a_number)
# # print("Rounded number is", rounded_value)

# # Data types
# number = 10
# print(number)
# print(type(number))

# floatingNumber =10.1
# print(floatingNumber)
# print(type(floatingNumber))

# roundNumber =5.147632
# rounded = round(roundNumber,3)
# print(rounded)

# condition =not False
# print(condition)
# print(type(condition))

# word = "stuff"
# print(word)
# print(len(word)) # calculates the length of the word

# converting a string into a float
# new_Number="10.53"
# floated_Number=float(new_Number)
# print(floated_Number)


# Multiplying a string by an integer
# a_string= "abc" *2
# print(a_string)

# def evaluate_number(numb):
#     if numb >= 20:
#         message = "number is greater than 20"
#     elif numb >= 10:
#         message = "number is greater than 10"
#     else:
#         message = "Number is greater than or equal to 0"
#     return message

# print(evaluate_number(21))

# Intro to Lists

# number_list= [1,2,3,4,5,6,7,8,9,10]
# print("Max:", max(number_list))
# print("Min:", min(number_list))
# print("Sum:", sum(number_list))
# avg = sum(number_list[2])/2
# print(avg)

# def a_test():
#     """
#     A test function
#     """
#     a_letter = "a"
#     return a_letter

# help(a_test)

# print("a","b","c",sep=" > ")

# def say_hello(person="Calvin"):
#     print("Hello,", person)

# say_hello()
# say_hello("world")

def can_get_license(age,no_criminal_history):
    return not no_criminal_history and (age>15.5)

print(can_get_license(14, False))
print(can_get_license(20, False))
print(can_get_license(16, False))
print(can_get_license(16, True))