def car_make(manufacturer,model_name,**other_info):
    other_info["manufacturer"] = manufacturer
    other_info["model_name"] = model_name
    return other_info

def build_profile(f_name,l_name,age):
    full_profile = f"{f_name.title()} {l_name.title()} is {age} years old"
    print(full_profile)