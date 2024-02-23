feeling=input("How are you feeling today?")
any_trouble=input("Did any trouble happen?")
if feeling.lower() == "great" and any_trouble.lower() == "no":
    print ("You are feeling {} today".format(feeling.lower()))
else:
    print("Oh no")