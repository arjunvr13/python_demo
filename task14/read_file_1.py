# Read and Print the Contents of a Text File
file_name = input("Enter the file name:")
mode = 'r'
try:
    with open(file_name,mode) as fp:
        print(fp.read())
except FileNotFoundError as e:
    print(e)