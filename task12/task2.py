import os
class Writeto:
    def __init__(self, filename, mode='w+'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file    
        
    def __exit__(self, exc_type, exc_value, traceback):
            self.file.seek(0)
            self.content = self.file.read()
            if 'bug' in self.content:
                self.file.close()
                print("'bug'is present in the file")
                os.remove(self.filename)
                print("file deleted")
            else:
                self.filename.close()
          

filename = "example"
text_input = input("Enter text to write to the file: ")
try:
    with Writeto(filename) as file:
        file.write(text_input)
except Exception as e:
    print("No 'bug' in the file")
