# Write a Python program to implement a binary search on a sorted list
def binary_search(list,low,high,key):
    while high > low:
        mid = (low+high)//2
        if list[mid] == key:
            return mid
        elif list[mid] > key:
            high = mid - 1
        elif list[mid] < key:
            low = mid + 1
    return -1

new_list = []
n = int(input("Enter the limit of the list:"))
print("Enter the number to the list:")
for i in range(0,n):
    value = int(input())
    new_list.append(value)
print(new_list)
new_list.sort()
print(new_list)
key = int(input("Enter the element to be searched:"))
result = binary_search(new_list,0,len(new_list)-1,key)
if result != -1:
    print("element found at position",str(result+1))
else:
    print("Not found")