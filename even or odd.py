def iseven(n):
    while n != 0:
        if n % 2 == 0:
            return "even"
        else:
            return "odd"
n=int(input("enter a number:"))
print(iseven(n))
