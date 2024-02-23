class Cypher:
    def __init__(self) -> None:
        self.str1 = str1
        self.encoded = self.encode()
        # print(self.str1)

    def encode(self):
        new_str = ""
        for i in self.str1:
            if i.isdigit():
                new_str += str(int(i)+1) if int(i) < 9 else '0'
            
            elif i.isalpha():
                if i.islower():
                    new_str += chr((ord(i) - ord('a') + 2) % 26 + ord('a'))
                else:
                    new_str += chr((ord(i) - ord('A') + 2) % 26 + ord('A'))
                new_str = new_str[:-1] + new_str[-1].swapcase()
            else:
                new_str += i 
        print("string after encoding:",new_str)
        return new_str

    def decoder(self):
        dec_str = ""
        for i in self.encoded:
            if i.isdigit():
                dec_str += str(int(i)-1) if int(i) > 0 else '9'
            elif i.isalpha():
                if i.islower():
                    dec_str += chr((ord(i) - ord('a') - 2) % 26 + ord('a'))
                else:
                    dec_str += chr((ord(i) - ord('A') - 2) % 26 + ord('A'))
                dec_str = dec_str[:-1] + dec_str[-1].swapcase()
            else:
                dec_str += i 

        print("string after decoding:",dec_str)
str1 = input("Enter the string:")
s1 = Cypher()
s1.decoder()