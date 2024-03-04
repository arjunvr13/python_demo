#Search for a String in a Text File
word = input("Enter the string:")
file_name = input("Enter the file name:")
mode = 'r'
try:
    with open(file_name,'r') as fp:
        # print(fp.read())
        # for line in fp:
        line = fp.read()
        if word in line:
            print(word," is present in the file")
        else:
            print(word,"is not present in the file")
except FileNotFoundError as e:
    print(e)
