#Count the Number of Lines, Words, and Characters in a Text File
count = 0
count_w = 0
count_c = 0
white_space = 0
with open("example","r") as fp:
    for line in fp:
        count += 1 
        count_w += len(line.split())
        count_c += len(line)
        white_space += sum(1 for char in line if char.isspace())
    print("count of line in the file:",count)
    print("count of words in the file:",count_w)
    print("count of character in the file(including white space):",count_c)
    print("total number of characters in the file:",count_c-white_space)
        

