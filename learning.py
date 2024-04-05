drivers_cars = {
    "john":"BMW",
    "jack":"ford",
    "bob":"BMW",
    "tristan":"ford"
}

bmw_count = 0
ford_count = 0
for driver, car in drivers_cars.items():
    if car == "ford":
        ford_count +=1
        print(f"{driver.title()} drives a {car.title()}")
    else:
        bmw_count +=1
        print(f"{driver.title()} drives a {car.title()}")

print(f"\nBMW count: {bmw_count}")
print(f"Ford count: {ford_count}")