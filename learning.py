# While loops
prompt = "Type in a word that you want to repeat\nEnter 'quit' to end the program: "
message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)
    else:
        print(f"Program is quitting because you entered {message}")


