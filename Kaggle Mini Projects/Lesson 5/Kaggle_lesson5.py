# Use the for loop
companies=["Google","Tesla","Microsoft","LG","Lucid","Chase","Logitech","Bank of America"]
for each_company in companies:
    print(each_company, end="  ")

# line breaker in the terminal
print("\n-----------------------------------")

# Use the range() fuction
for i in range(8):
    print(companies[i])


# line breaker in the terminal
print("\n-----------------------------------")


# Use the while loop
a_number=0
while a_number < 3:
    print(companies[a_number])
    a_number+=1


# line breaker in the terminal
print("\n-----------------------------------")


# Use a list comprehension | Use a list comprehension which uses a conditional statement
five_letters=[five for five in companies if len(five)<6]
print(five_letters)

