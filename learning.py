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
# current_users = ["john","jake","BOB","steve","tristan","J"]
# new_users = ["Steve","bob","ashly","leila","moran","j"]
# lowerCased=[word.lower() for word in current_users]
# matched_names=[]
# print(lowerCased)
# for every_new_user in new_users:
#     if every_new_user.lower() in lowerCased:
#         print(f"Matched name: {every_new_user.lower()}")
#         matched_names.append(every_new_user.lower())
#     else:
#         print(f"This name isn't repeated: {every_new_user.lower()}")
# print(f"\nAll matched names: {matched_names}")


#5-11. Ordinal Numbers
numbers = [1,2,3,4,5,6,7,8,9]
for every_number in numbers:
    if every_number == 1:
        print("1st")
    elif every_number == 2:
        print("2nd")
    elif every_number == 3:
        print("3rd")
    else:
        print(f"{every_number}th")
