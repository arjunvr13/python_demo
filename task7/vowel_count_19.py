# Write a Python program to count the number of vowels in a string
String = input("Enter the string:")
print(String)
count = 0
for i in range(len(String)):
    if((String[i] == 'a') or(String[i] == 'e') or(String[i] == 'i') or (String[i] == 'o') or(String[i] == 'u')):
        count += 1
print("vowels:",count)