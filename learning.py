unconfirmed_users = ["john","jack","bob"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying {current_user.title()}")
    confirmed_users.append(current_user)

print(f"Here are the confirmed users:")
for every_confirmed_user in confirmed_users:
    print(every_confirmed_user.title())