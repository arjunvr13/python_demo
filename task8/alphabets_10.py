# · Write a Python program to create a file where all letters of English alphabet 
# are listed by specified number of letters on each line.
def alphabet_group(n, f):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    with open(f, 'w') as file:
        for i in range(0, len(alphabet), n):
            line = alphabet[i:i+n]
            file.write(line + '\n')

    print("Success file created")

n = int(input("Enter the number"))
f = 'alphabet.txt'
alphabet_group(n, f)
