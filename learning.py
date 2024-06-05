#8-14. Cars
def car(manufacturer,model_name,**other_info):
    other_info["manufacturer"] = manufacturer
    other_info["model_name"] = model_name
    return other_info

first_car = car("Tesla","Model Y", wheels = 4, color = "blue", safe = True)
print(first_car)