def doublelist(li):
    newlist=[]
    for i in range(0,len(li)):
        result=li[i]*li[i]
        newlist.append(result)
    return newlist

print(doublelist([1,2,3,4,5,6,7]))
