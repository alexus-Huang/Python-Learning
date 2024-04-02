# #5-8. Hello Admin
usernames =[]
# for every_name in usernames:
#     if every_name == "admin":
#         print(f"Hello {every_name}")
#     else:
#         print(f"{every_name.title()} logged in")
    
#5-9. No Users
if usernames:
    for every_name in usernames:
        if every_name == "admin":
            print(f"Hello {every_name}")
        else:
            print(f"{every_name.title()} logged in")
else:
    print("We need some users!")