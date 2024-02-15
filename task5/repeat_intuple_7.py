# Write a Python program to find the repeated items of atuple.

tuple1 = (int(x) for x in input("Enter any value:").split())
in_list = []
dup = []
for i in tuple1:
    if i not in in_list:
        in_list.append(i)
    elif i not in dup:
        dup.append(i)
res = tuple(dup)
print(res)
