my_list = [3,4,5,2,1,5,4,2,3,4,56,7,8,5,3,5,2,2,4]
print("Original:", my_list)
my_list.sort()
print("Sorted:", my_list)
my_list.insert(2, 55555555)
print("Inserted", my_list)
my_list.append(777)
print("Appended", my_list)
my_list.remove(1)
print("Removed", my_list)
my_list.reverse()
print("Reversed", my_list)
del my_list[2]
print("Deleted", my_list)

total = 0
for x in my_list:
    total += x
print("Total", total)

average = 0
running_average = 0
for av in my_list:
    running_average += av
    average = running_average/len(my_list)
print("Average", average)