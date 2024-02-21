#Write a Python program to copy the contents of a file to another file.
f = open("text", "r")
f1 = open("text_copy", "w")
for data in f:
    f1.write(data)
f1.close()