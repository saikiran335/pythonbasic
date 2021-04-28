try:
    f=open("sai.txt")
    f.write("hello welcome")
except:
    print("something went wrong")
finally:
    
    print("process completed")
