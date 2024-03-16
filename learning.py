guest_list= ["John Doe", "Jane Doe","Bob","Jack","Dave"]
print(f"This is the guest list: {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}")

# 3.5 - changing the guest list
unable = "Bob"
guest_list.remove(unable) # Remove BOb from guest_list
print(f"Looks like: {unable} can't make it.")
replacement= "Zack"  # Set a variable and assign a value of who is replacing Bob
guest_list.append(replacement) # Add in the person that will be replacing Bob
print(f"This is the guest list: {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}")  # Print the new list


# 3.6 - More Guests
print("Looks like we found a bigger table\n")
guest_list.insert(0,"Pheobe") # add a new person to the start of the list 
guest_list.insert(2,"Scott") # add a new person into the middle of the list
guest_list.append("Jesse") # add a new perosn to the end of the list
print(f"This is the guest list: {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, {guest_list[5]}, {guest_list[6]}, {guest_list[7]}")  # Print the new list


# 3.7 - Shrinking Guest List
print("Only 2 people can come to the party")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")
print(f"Sorry {guest_list.pop()}, you can't come")

# Announce the 2 people that are allowed to come to the party
print(f"These 2 people are allowed to come to the party: {guest_list[0]}, {guest_list[1]}")
print(guest_list)
# Print an empty list
print(f"{guest_list.pop()} was removed from the invitation list")
print(f"{guest_list.pop()} was removed from the invitation list")
print(guest_list)