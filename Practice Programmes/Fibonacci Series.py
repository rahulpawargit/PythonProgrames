series = int(input("Enter number to genarate Fibonacci Series"))
n1 = 0
n2 = 1
count = 0
while count < series:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count = count + 1


