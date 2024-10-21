fact = 1
num  = 5

if num < 0 :
    print("number is Zero")
else:

    for i in range(num):
        fact = fact * num
        num = num -1

    print(fact)