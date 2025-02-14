# lst = [1,5,7,2,3,9,0,8,7,9]
#
# largest = 0
# second_largest = 0
#
# for num in lst:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest  = num
#
# print(second_largest )

# def find_secondLargest(numbers):
#
#     largest = 0
#     second_largest = 0
#
#     for num in numbers:
#         if num > largest:
#             second_largest = largest
#             largest = num
#
#         elif num > second_largest and num!= largest:
#             second_largest = num
#
#     return second_largest
#
# numbers = [1,5,3,5,6,8,4,0,7,10, 9]
# print(find_secondLargest(numbers))

lst = [2, 4, 5, 3, 7,3, 10]

largest = 0
second_larg = 0

for i in lst:
    if i > largest:
        second_larg = largest
        largest = i

    elif i > second_larg and i != largest:
        second_larg = i

print(second_larg)
# print(largest)
