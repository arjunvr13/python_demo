# Write a Python program to merge two sorted lists into a single sorted list.
list_1 = [1,2,5,3,4]
list_2 = [2,3,4,6,7]
list_1.sort()
list_2.sort()
print("The list after merging list1 and list2:",list_1+list_2)