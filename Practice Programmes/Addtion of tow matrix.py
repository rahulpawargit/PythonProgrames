# x = [[12, 3, 8],
#      [5,6,7],
#      [5,7,2]]
#
# y = [[5,6,7],
#      [7,5,4],
#      [5,6,1]]
#
# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]
#
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + y[i][j]
#
# for r in result:
#     print(r)


lst1=[[65,6,7]]
lst2=[[8,7,6]]

res=[ [0,0,0]]

for i in range (len(lst1)):
    for j in range(len(lst1[0])):
        res[i][j]= lst1[i][j] + lst2[i][j]

for r in res:
    print(r)