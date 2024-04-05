person1 = {
    "first_name": "john",
    "last_name" : "doe",
    "city" : "SF"
}
person1_firstName = person1["first_name"].title()
person1_lastName = person1["last_name"].title()
person1_city = person1["city"]
print(f"{person1_firstName} {person1_lastName} is from {person1_city}")