# #5-8. Hello Admin
usernames =[]
# for every_name in usernames:
#     if every_name == "admin":
#         print(f"Hello {every_name}")
#     else:
#         print(f"{every_name.title()} logged in")
    
#5-9. No Users
# if usernames:
#     for every_name in usernames:
#         if every_name == "admin":
#             print(f"Hello {every_name}")
#         else:
#             print(f"{every_name.title()} logged in")
# else:
#     print("We need some users!")

#5-10. Checking Usernames
current_users = ["john","jake","BOB","steve","tristan","j"]
new_users = ["Steve","bob","ashly","leila","moran","j"]
lowerCased=[word.lower() for word in current_users]
print(lowerCased)
for every_new_user in new_users:
    if every_new_user.lower() in lowerCased:
        print(f"Matched name: {every_new_user.lower()}")
    else:
        print(f"This name isn't repeated: {every_new_user.lower()}")
