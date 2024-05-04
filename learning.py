odd_numbers = []
current_numbers = 0
while current_numbers < 10:
    current_numbers+=1
    if current_numbers % 2 == 0:
        continue
    odd_numbers.append(current_numbers)
print(odd_numbers)