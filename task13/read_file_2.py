try:
    with open("example1",'r') as fp:
        print(fp.read())
except FileNotFoundError:
    print("File Does not Exists")