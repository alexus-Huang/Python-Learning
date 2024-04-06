drivers_cars = {
    "john":"BMW",
    "jack":"ford",
    "bob":"BMW",
    "tristan":"ford"
}

friends = ["john","bob"]
for name in sorted(drivers_cars.values()):
    print(f"{name.title()}")