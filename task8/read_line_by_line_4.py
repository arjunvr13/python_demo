# Write a Python program to read a file line by line store it into a variable.
f = open("text","r")
for i in f:
    data = f.readlines()
print(data)
f.close()