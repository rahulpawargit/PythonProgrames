# num = int(input("Enter a number"))
#
# sum = 0
# temp = num
#
# while temp > 0:
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#
# if num == sum:
#     print("Number is arm")
# else:
#     print("Number is not arm")


#internval of Argmstrong number

lower = 100
upper = 500

for num in range(lower, upper+1):
    sum= 0
    temp = num


    while temp > 0:
        arm = temp % 10
        sum +=arm ** 3
        temp //=10

    if num== sum:
        print(num)


