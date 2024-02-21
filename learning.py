# amount = 2 #Variable assignment

# print(amount) #Function calls

# if amount == 2: #Conditionals. The colon indicates a new code block
#     print("Equal to 2")

# word_spamming = "test " * amount  # * operator is used to multiply numbers and strings
# print(word_spamming)

# print(type(word_spamming)) # Tells us what word_spamming is
# # int - short for integer
# print(int('807') + 1) # Turns "807" -> 807 then adds it to 1  -> = 808
# # float - a number with decimal values

# #Basic arithmetic
# print(3+5)
# print(10//3) # the // operator gives us a value thats rounded down
# print((10/2)+9) # the () are used to specify which values should be simplified first

# # min and max builtin functions
# print(min(2,5,3))
# print(max(2,5,3))

# #abs function - stands for absolute

# print(abs(-32))


# Lists
# cars=["BMW","Nissan","Toyota","Ford","Tesla","Lucid"]
# cars.clear()
# print(cars)



# Tuples
# test=[1,2,3,4,5,]
# test.insert(0,100)
# print(test)

# for loops
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for every_planet in planets:
#     print(every_planet,end=" ")

# range() function
# for i in range(3):
#     print(i+1)

# while loops
# i=0
# while (i<10):
#     i+=1
#     print(i)

# List comprehension
negative_numbers=[5, -1, -2, 0, 3]
how_many_neg_numbers=[neg_num for neg_num in negative_numbers if neg_num<0]
print(how_many_neg_numbers)