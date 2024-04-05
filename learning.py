# 6-1. Person
person1 = {
    "first_name": "john",
    "last_name" : "doe",
    "city" : "SF"
}
person1_firstName = person1["first_name"].title()
person1_lastName = person1["last_name"].title()
person1_city = person1["city"]
print(f"{person1_firstName} {person1_lastName} is from {person1_city}")

# 6.2 - Favorite Numbers
fav_nums = {
    "john": 1,
    "tristan": 2,
    "jack" : 3,
    }
print(f"John's favorite number is {fav_nums['john']}")
print(f"Tristan's favorite number is {fav_nums['tristan']}")
print(f"Jack's favorite number is {fav_nums['jack']}")
