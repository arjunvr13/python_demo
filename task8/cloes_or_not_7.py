# Write a Python program to assess if a file is closed or not.
f = open("text","r")
print(f.closed)
if f.closed == False:
    print("not closed")
else:
    print("The file is closed")