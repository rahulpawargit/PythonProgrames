# X = [[2,3,5,8],
#      [5,6,8,1]]
#
# Y = [[7,6,8,7,],
#      [8,7,5,9]]
#
# result = [[0,0,0,0],
#           [0,0,0,0]]

# Program to multiply two matrices using nested loops

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
#
# for i in range(len(X)):
#     for j in range(len(Y[0])):
#         for k in range(len(Y)):
#             result[i][j]= X[i][k] * Y[k][j]

for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)