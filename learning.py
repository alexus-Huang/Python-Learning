# *args

def add(*all_numbers):
    sum = 0
    for i in all_numbers:
        sum+=i
    print(sum)

add(1,2,3,4,5,6)