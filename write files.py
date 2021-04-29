f=open("D:\python basics\pythonbasic\slicing.py","a")
f.write("'this is end of the program'")
f.close()


f=open("D:\python basics\pythonbasic\slicing.py","r")
for x in f:
    print(x)
f.close()
