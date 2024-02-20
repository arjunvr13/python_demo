# Write a Python program to check if a string is an anagram of another string.("listen", "silent")
string_1 = input("Enter the First string:")
string_2 = input("Enter the First string:")
print(string_1)
print(string_2)
list_1 = sorted(list(string_1))
list_2 = sorted(list(string_2))
print(list_1)
print(list_2)
if list_1 == list_2:
    print("Anagram")
else:
    print("Not an Anagram")