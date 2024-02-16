# Create a function that takes a string and returns a dictionary where keys are letters,
# and values are the number of times each letter appears in the string

def string_dict(string):
    print(string)
    unique = list(string.lower())
    dict = {}
    for i in unique:
        if i != ' ':
            dict[i] = unique.count(i)
    return(dict)


string = input("Enter the string:")
result = string_dict(string)
print("Letter of the string as key and the count of the letter as values:",result)


