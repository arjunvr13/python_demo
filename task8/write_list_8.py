#Write a Python program to write a list to a file.
new_list = []
n = int(input("Enter the number of elements :"))
print("Enter the number to the stack:")
for i in range(0,n):
    value = int(input())
    new_list.append(value)
print(new_list)
f1 = open("abc","w")
f1.write(str(new_list))
print("success")