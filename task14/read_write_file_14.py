class FileOperations:
    file_name = "abc"

    @classmethod
    def addText(cls,in_text):
        with open(cls.file_name,"+w")as fw:
            fw.write(in_text)
        print("text writtte successfully")
    
    def appendText(cls,in_text):
        with open(cls.file_name,"a")as fa:
            choice = input("Enter the choice same line or next line(same/next):")
            if choice == 'same':
                fa.write(" "+in_text)
            elif choice == 'next':
                fa.write("\n"+in_text)
            else:
                print("Invalid choice")
        print("text append successfull")

    @classmethod
    def readNote(cls):
        with open(cls.file_name,"r") as fr:
            content = fr.read()
            # for lines in content:
            #     print(lines)
            if not content:
                return "No Notes found"
            return content
        

files = FileOperations()
while True:
    print("\n1 - Write Note (Overwrite existing).")
    print("2 - Add more Notes (Append).")
    print("3 - Read Notes.")
    print("4 – Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        in_text = input("\nEnter the text to be entered:")
        files.addText(in_text)

    elif choice == 2:
        in_text = input("\nEnter the text to be entered:")
        files.appendText(in_text)
    elif choice == 3:
        print("\n**Content of the file**")
        print(files.readNote())
    else:
        break