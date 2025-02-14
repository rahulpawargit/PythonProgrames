# add two nested lists
from functools import reduce

list = [[1, 2],[ 1, 3, 4,], [4, 7]]

newlist= sum(list, [])
print(newlist)
# print(reduce(lambda x, y: x+y, list))