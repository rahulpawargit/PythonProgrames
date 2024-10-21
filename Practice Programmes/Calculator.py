def add(x, y):
    return x + y

def sub(x, y):
    return (x - y)

def multi(x, y):
    return (x * y)

def dev(x, y):
    return (x/y)

choice = input("Enter values in 1/ 2/ 3/ 4 format")

if choice in ('1', '2', '3','4'):

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("addtion is ", add(num1, num2))
    elif choice == '2':
        print("substration is ", sub(num1, num2))
    elif choice == '3':
        print("Multiplication is ", multi(num1, num2))
    elif choice == '4':
        print("devistion is ", dev(num1, num2))
