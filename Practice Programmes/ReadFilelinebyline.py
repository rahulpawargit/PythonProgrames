# with open("C:\\New folder (2)\\Test.txt") as f:
#     content_list = f.readlines()
#     print(content_list)
#
#     # # print(content_list,end=' ')
#     content_list = [x.strip() for x in content_list]
#     print(content_list)


# import random
# lst = [1, '3', 'c', 23, 234]
# print((random.choice(lst)))

#write in file

file = open(("C:\\New folder (2)\\Test.txt"))
contest_list= file.readlines()
print(contest_list)
contest_list= [x.strip() for x in contest_list]
print(contest_list)