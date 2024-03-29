# 4-10. Slices
items=["pizza","hotdog","pretzel","pepporoni","sausage","bread","eggs","water"]
print(f"The first 3 itmes in the list are: {items[:3]}")  # Print the first 3 items in a list
print(f"Three items from the middle of the list are: {items[3:6]}") # Print the 3 items in the middle of the list
print(f"The last 3 items in the list are: {items[-3:]}") # Print the last 3 items in the middle of the list

#4-11. My Pizzas, Your Pizzas:
copied_list = items[:]
copied_list.append("New item")
copied_list.append("Second new item")
print(f"\nOriginal list: {items}\nCopied list: {copied_list}\n")
for every_original_item in items:
    print(every_original_item)
print("\n")
for every_copied_item in copied_list:
    print(every_copied_item)