how_many_tires=int(input("How many tires do you have on your vechile "))
if how_many_tires==4 or how_many_tires==3:
    print("You currently have {} tires on your vechile!".format(how_many_tires))
elif how_many_tires > 4:
    print("You have more than 4 tires!")
else:
    print ("You don't have a car")