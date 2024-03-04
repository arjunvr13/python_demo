# Python program to delay printing of line from a file using sleep function
from time import sleep
in_file = input("Enter the file name:")
with open(in_file, "r")as fr:
    for line in fr:  
        print(line)
        sleep(2)