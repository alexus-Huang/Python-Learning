new_users = ["john","joe","dave"]
registered_users = []

def register_ppl(new_users,registered_users):
    while new_users:
        registering_users = new_users.pop()
        print(f"Registering {registering_users.title()}")
        registered_users.append(registering_users)

def show_registered_ppl(registered_users):
    for every_user in registered_users:
        print(f"\nRegistered {every_user.title()}")


register_ppl(new_users[:],registered_users)
show_registered_ppl(registered_users)
print(new_users)