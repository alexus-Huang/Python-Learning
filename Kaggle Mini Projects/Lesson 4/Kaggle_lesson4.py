# Create a list that has 5 elements
my_list=["a","word","third","fourth","fifth"]

# Find the second element
second_element=my_list[1]
print("Second element:", second_element)

# Find the last element
last_element=my_list[-1]
print("Last element:", last_element)

# Find the first 2 elements
first_two_elements=my_list[:2]
print("First 2 elements:", first_two_elements)

# Find every element after the first 2 elements
every_element_after_first_two=my_list[2:]
print("Every element after the first 2 elements:", every_element_after_first_two)

# Find the last 2 elements
last_two_elements=my_list[-2:]
print("Last 2 elements:", last_two_elements)

# Change the first element to a number
changing_first_element=2
my_list[0]=changing_first_element
print(my_list)

# Find the length of the list
print("Length of the list is:", len(my_list))

# Add a new item to the end of the list
new_item_at_end="End"
my_list.append(new_item_at_end)
print(my_list)

# Add a new item to the start of the list
new_item_at_start = "Start"
my_list.insert(0, new_item_at_start)
print(my_list)

# Remove the last item of the list
print("Last item of the list that was removed:", my_list.pop())

# Find the index of the second element
print(my_list.index("word"))

# Determine whether an element is in the list
print("fourth" in my_list)

# Create a tuple
tupe1= (1,2,3)
print(type(tupe1))