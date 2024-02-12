# Write a Python function that accepts a string and counts the number of upper and lower case letters.
def count_upper_n_lower(s):
    ucount = 0
    lcount = 0
    for i in s:
        if i.isupper():
            ucount += 1
        else:
            lcount += 1
    print("count of upper case letters",ucount)
    print("count of lower case letters",lcount) 

s = input("Enter the string:")
count_upper_n_lower(s)