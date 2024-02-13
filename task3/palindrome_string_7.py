# Write a Python program to find palindromes in a given list of strings using Lambda

def reverse(words):
    result = list(filter(lambda x :(x == "".join(reversed(x))),words))
    print(result)
str = input("Enter the list of strings:")
words = str.split(" ")
print(words)
reverse(words)

