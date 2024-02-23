feeling=input("How are you feeling today? ")
if not(feeling.lower() == "great"):
    print("Oh no")
else:
    print("You are feeling {}".format(feeling))