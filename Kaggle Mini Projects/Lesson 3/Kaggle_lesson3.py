# Assign 2 variables 2 possible values of bool
first_variable = True
second_variable = False

# Define a function that uses booleans to return an answer
def can_you_drive(age):
    return age>15.5
print(can_you_drive(17))
print(can_you_drive(14))

# In a function, combine boolean values (and, or, not)
def can_you_drive_second(current_age,criminal_history):
    return (current_age >=15.5) and not criminal_history

print(can_you_drive_second(16, False))

# Write a conditional statement
third_variable = 12
if third_variable == 15:
    print(15)
else:
    print("Not 15")


# Use the print() function and take the bool() function as an argument and input integers and strings to see the output
print(bool("Word"))
print(bool(0))
print(bool(1))
print(bool(""))