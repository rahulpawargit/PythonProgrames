#Higest Commen Devider or Gretest Commen Devider.

# def compute_hcf(x, y):
#
# # choose the smaller number
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
#
# num1 = 12
# num2 = 10
#
# print("The H.C.F. is", compute_hcf(num1, num2))



def compute_scd(x, y):

    if (x < y):
        t = x
    else:
        t = y
    for i in range(t, t+1):
        if (x % i == 0) and ( y % i == 0):
            scd = i
    return scd

n1 = 40
n2 = 80

print(compute_scd(n1, n2))
