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
print(f"Here is the list of locations in reverse-alphabetical order: {locations}")