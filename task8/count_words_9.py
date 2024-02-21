#Write a Python program that takes a text file as input and returns the number of words of a given text file.
#Note: Some words can be separated by a comma with no space.

n = 0
with open('text_copy','r') as file:
	data = file.read()
	print(data)
	new = data.replace(","," ")
	lines = new.split()
	n += len(lines)
print("No of words =",n)

