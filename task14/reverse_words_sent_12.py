# Write a function that takes a sentence as input and returns a new sentence
# with the words reversed, while keeping the order of the words in the
# sentence.
def reverseWords(s):
    out =[]
    seperate_list = s.split(' ')
    # print(list(seperate_list))
    for i in seperate_list:
        re_list = list(i)
        out.append(re_list[::-1])
    # print(out)
    converted_string = ' '.join([''.join(in_list) for in_list in out])
    return converted_string

s = input("Enter the string:")
print(s)
result = reverseWords(s)
print(result)