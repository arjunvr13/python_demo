list1 = [1,2,3,'e','e',4,89,1]
print(list1)
in_list = []
duplicate = []
for i in list1:
    if i not in in_list:
        in_list.append(i)
    elif i not in duplicate:
        duplicate.append(i)
print(duplicate)