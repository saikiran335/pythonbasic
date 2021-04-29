f=open("abc.py","w")
f.write("hi hello how r u")
f.close()


f=open("abc.py","r")
for x in f:
    print(x)
f.close()
