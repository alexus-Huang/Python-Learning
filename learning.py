rivers={
    "nile":"egypt",
}
for river_name in rivers:
    print(f"River name: {river_name.title()}")

for river_location in rivers.values():
    print(f"River location: {river_location.title()}")