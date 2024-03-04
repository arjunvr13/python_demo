#Count the total number of uppercase characters in a file in Python
in_file = input("Enter the file name:")
with open(in_file,'r') as fr:
    res_list = fr.readlines()
    count = 0
    for line in res_list:
        # line.split()
        new_list = list(line)
        # print(new_list)
        for i in new_list:
            if i.isupper():
                count += 1
print("Number of Uppercase Characters:",count)


# new_list = []
# with open("example","r")as fr:
#     res_list = fr.readlines()
#     count = 0
#     for line in res_list:
#         list_remove = line.strip('\n')
#         new_list.append(list_remove)
#     res = [char for word in new_list for char in word]
#     print(res)
#     for i in res:
#         if i.isupper():
#             count += 1
# print("Number of Uppercase Characters:",count)
