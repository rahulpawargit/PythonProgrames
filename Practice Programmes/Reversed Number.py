num = 1245
reversed_num = 0

while num != 0:
    rem = num % 10
    reversed_num = reversed_num * 10 + rem
    num //= 10

print(str(reversed_num))
################
num1 = 4568
print( str(num1)[::-1])


