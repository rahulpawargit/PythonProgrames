# fact = 1
# # num  = 5
# num =4
# if num < 0 :
#     print("number is Zero")
# else:

    # for i in range(num):
    #     fact = fact * num
#     #     num = num -1
# while num > 0:
#     fact = fact * num
#     num = num -1
#
# print(fact)

num = int(input("Enter a number to find factorial"))
fact = 1

while num > 0:
    fact = fact * num
    num = num -1

print(fact)
