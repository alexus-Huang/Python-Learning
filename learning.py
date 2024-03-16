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
guest_list.insert(0,"Pheobe")
guest_list.insert(2,"Scott")
guest_list.append("Jesse")
print(f"This is the guest list: {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, {guest_list[5]}, {guest_list[6]}, {guest_list[7]}")