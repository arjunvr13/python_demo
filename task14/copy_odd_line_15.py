# Copy odd lines of one file to another file in Python
in_file = input("Enter the file name:")
out_file = input("Enter the file name that contain the output:")
with open(in_file,"r") as fr:
    re_list = fr.readlines()
    with open(out_file,"w") as fw:
        length = len(re_list)
        for i in range(0,length):
            if (i+1) % 2 == 1:
                    fw.write(re_list[i])
            else:
                pass