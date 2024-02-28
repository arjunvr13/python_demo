
try:
    # with open('example','r') as fp:
    #     with open('new','w') as nf:
    #         for line in fp:
    #              nf.write(line)
    fp = open('example','r')
    content = fp.read()
    fp.close()
    np = open('new','w')
    np.write(content) 
    # np.close()
    # print(np.closed)
    if not np.closed:
        raise IOError
except IOError:
    print("file not closed")
finally:
    np.close()
    print("The file was closed using finally")
    # print(np.closed)