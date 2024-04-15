#6-7 People
people = {
    "john":{
        "first":"john",
        "last" : "doe",
        "age": 30
    },
    "jack":{
        "first":"jack",
        "last":"brown",
        "age":35
    },
    "jane":{
        "first":"jane",
        "last":"doe",
        "age":40
    }
}

for every_person,detail in people.items():
    print(f"Name: {every_person}")
    full_name = f"{detail['first']} {detail['last']}"
    age = f"{detail['age']}"
    print(f"Description:\n\t{full_name.title()}\n\tAge: {age}")