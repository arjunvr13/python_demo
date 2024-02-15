# Write a Python program to count the number of strings where the string length is 2 or more.
# 	Sample List : ['abc', 'xyz', 'aba', '1']
# 	Expected Result : 3
list2 = ['abc', 'xyz', 'aba','1']
# n = int(input("Enter the limit:"))
# for i in range(0,n):
#     string = input("Enter the string:")
#     list2.append(string)
# print(list2)

count = 0
for i in range(len(list2)):
    length = len(list2[i])
    if length >= 2:
        count += 1
print(count)