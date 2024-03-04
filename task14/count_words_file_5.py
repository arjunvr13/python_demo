# Implement a program that reads a text file and counts the occurrences of
# each word, ignoring case sensitivity. 
def counter(list_new):
    #print(list_new)
    dict = {}
    for i in list_new:
        if i != ' ':
            dict[i] = list_new.count(i)
    return dict



list_new = []
with open("example",'r') as file_read:
        # print(file_read.read())
        for line in file_read:
            list_li = line.split()
            words = [word.strip().lower() for word in list_li]
            list_new.extend(words)
            # print(list_li)
        # print(list_new)
        result = counter(list_new)
        print(result)