mylist = [23,26,65,452,196,13,2,4]

result = list(filter(lambda x:(x % 2 ==0), mylist))
print("Number is divisible by 2  are", result)