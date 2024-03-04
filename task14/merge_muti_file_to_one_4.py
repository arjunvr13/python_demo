# Merge Multiple Text Files into One
# def merge_file(in_files,out_file):
#     with open('out_file','w') as fw:
#         for in_file in in_files:
#             with open(in_file,"r") as fr:
#                 fw.write(fr.read())
#                 fw.write("\n")


# in_files = ['a','b','c']
# out_file = 'out_file'
# merge_file(in_files,out_file)
def create_file(file_name,mode):
    data = input("Enter the string:")
    with open(file_name,mode) as file_write:
        file_write.write(data)
    return file_name

        

def merge_file(in_files):
    out_file = input("Enter the name of the file to store the merged content:")
    with open(out_file,'w') as fw:
        for in_file in in_files:
            with open(in_file,"r") as fr:
                fw.write(fr.read())
                fw.write("\n")


in_files = []
n = int(input("Enter the number of files:"))
for i in range(n):
    file_name = input("Enter the file name:")
    mode = 'w'
    in_files.append(create_file(file_name,mode))
# print(in_files)
merge_file(in_files)