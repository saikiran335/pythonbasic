

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def mod(x, y):
    return x % y

def exp(x, y):
    return x ** y

def div(x, y):
    return x // y

print("""Enter numbers from 1 to 7
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Modulo
        6. Exponent
        7. Floor division""")

while True:

    choice = input("Enter choice: ")


    if choice in ('1', '2', '3', '4' , '5' , '6' , '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1, num2))
        elif choice == '6':
            print(num1, "^", num2, "=", exp(num1, num2))
        elif choice == '7':
            print(num1, "//", num2, "=", div(num1, num2))
    
        break
    else:
        print("Invalid Input")
    
        
