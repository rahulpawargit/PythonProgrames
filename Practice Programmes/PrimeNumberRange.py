
lowernumber = 100
highternubmer = 200

for num in range(lowernumber, highternubmer + 1):
    if (num > 1 ):
        for i in range(2, num):
            if num % i == 0:
                break

        else:
                print(num)
