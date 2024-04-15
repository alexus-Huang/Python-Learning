# #6-7 People
# people = {
#     "john":{
#         "first":"john",
#         "last" : "doe",
#         "age": 30
#     },
#     "jack":{
#         "first":"jack",
#         "last":"brown",
#         "age":35
#     },
#     "jane":{
#         "first":"jane",
#         "last":"doe",
#         "age":40
#     }
# }

# for every_person,detail in people.items():
#     print(f"Name: {every_person}")
#     full_name = f"{detail['first']} {detail['last']}"
#     age = f"{detail['age']}"
#     print(f"Description:\n\t{full_name.title()}\n\tAge: {age}")

# 6-8. Pet
pets = {
    "husky":{
        "owner": "Pheobe Brown",
        "animal age": 35
    },
    "maltese":{
        "owner":"John Doe",
        "animal age": 40 
    }
}
for each_pet,pet_detail in pets.items():
    print(f"{each_pet}")
    pet_owner_name = f"{pet_detail['owner']}"
    pet_animal_age = f"{pet_detail['animal age']}"
    print(f"\t Description:\n\t\tOwner:{pet_owner_name}\n\t\tAnimal Age:{pet_animal_age}")