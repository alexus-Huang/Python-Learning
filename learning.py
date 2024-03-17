# 3-8 Seeing the World

locations = ["California","Arizona","Texas","Chicago","Japan"] # 5 places to visit
print(f"Here is the original list: {locations}") # Show the user the 5 locations
print(f"Here is the sorted locations: {sorted(locations)}") # Print the temporary sorted list of locations
print(f"Here is the original list again: {locations}") # Show that the 5 locations are still in its original order
print(f"Here is the list in reverse-alphabetical order: {sorted(locations,reverse=True)}")
print(f"Here is the original list again: {locations}") # Show that the 5 locations are still in its original order
locations.reverse() # Reverse the order of the locations
print(f"Here is the list in reverse:{locations}") # Show the reversed list
locations.reverse() # Reverse the order of the locations again
print(f"Here is the list in reverse:{locations}") # Show the original list
locations.sort() # Permanently sort the list
print(f"Here is locations in alphabetical order:{locations}") # Show that the list has been permanently sorted
locations.sort(reverse=True)
print(f"Here is the list of locations in reverse-alphabetical order: {locations}\n")


# 3-9. Dinner Guests (Tell how many guests there are)
guests=["bob","john","jack","joseph","bryan","calvin","caleb"]
print(f"This is how many people are invited to the part: {len(guests)}\n")

# 3-10. Every Function
vechiles = ["Truck","Sedan","SUV"]
print(f"First element in the locations list: {locations[0].upper()}") # Show the first element from the locations list
guests[0]="Steve" # Change the first element in the guests list
print(f"The first person on the list is now: {guests[0]}") # Show who the first person is in the guests list
locations.append("Florida") # Add an element to the end of the locations list
print(f"This is the list of the locations: {locations}")
vechiles.insert(0,"Motorcycle") # Insert a new element to the first positon of the list
print(f"This is the list of vechiles: {vechiles}")
del vechiles[3] # Permanently delete the fourth value in the vechiles list
print(f"This is the new list of vechiles: {vechiles}")
removed_vechile=vechiles.pop()
print(removed_vechile)
vechiles.remove("Truck") # Removed 'Truck' from the list without knowing the index of the element
print(f"Here is the new list of vechile(s): {vechiles}\n") # Print out the new list

# Organizing a list (still 3-10. Every Function)
vechiles.append("Monster Truck")
vechiles.append("Mini-Cooper")
vechiles.append("Sedan")
print(f"This is the new list of vechiles: {vechiles}")
vechiles.sort()
print(vechiles)
print(f"This is the length of the vechile list: {len(vechiles)}")