from pathlib import Path

path = Path("guest.txt")
current_names = ""
while True:
    username = input("Name: ")
    if username.lower() == "quit":
        break
    else:
        current_names += f"Username:{username}\n"
        path.write_text(current_names)
