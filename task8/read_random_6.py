#Write a Python program to read a random line from a file.
import random
with open("text","r") as f1:
    lines = f1.readlines()
    print(random.choice(lines))
