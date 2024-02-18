print(help(round)) # use the help() function
print(round(5.546351,3)) # use the round() function
print("T",3,"X","T",sep=" - ") # use the sep argument in the print() function

def calculate(x,y,z): # define your own function
    """
    calculate() calculates the total and difference of the given numbers
    """
    total = x+y+z
    difference = abs(x-y-z)
    return total, difference
print(calculate(1,2,3))
print(help(calculate)) # use the help() function and put it in your function name as the argument
