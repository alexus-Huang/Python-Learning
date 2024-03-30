conditions = [True,False,False,True,True]
true_counter = 0
false_counter = 0
for each_condition in conditions:
    if each_condition == True:
        true_counter+=1
    else:
        false_counter+=1

print(true_counter)
print(false_counter)