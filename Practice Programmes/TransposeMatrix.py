#Transpose a matrix meaning swapping columns into rows

lst = [[12,4],
       [8,9],
       [8,6]]

result = [[0,0,0],
          [0,0,0]]

for i in range(len(lst)):
    for j in range(len(lst[0])):

        result[j][i]=lst[i][j]

for r in result:
    print(r)