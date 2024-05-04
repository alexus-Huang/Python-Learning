prompt = "Type out the letter f to continue: "
active = True

while active:
    message = input(prompt)
    if message != "f":
        active = False
    else:
        continue