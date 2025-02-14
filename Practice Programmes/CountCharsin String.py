# str_1 = "This is my first string"
# count = 0

# char1 = print(input((str("Etner char to count "))))
# char1 = 'i'
# for i in str_1:
#     if i == char1 :
#         count = count + 1
# print(count)

# def find_occurances(s, ch):
#     return [i for i, letter in enumerate(s) if  letter == ch]
#
#
# string1 = "Find the occurances of each character "
# ch = " "
# find_occurances(string1,ch)
#

string1 = "ffind the occurances of each character "
freq = {}
#
# for ele in string1:
#     if ele in  freq:
#         freq[ele] += 1
#     else:
#         freq[ele] = 1
# print("occurances of each characcter", freq)

for ele in string1:
    if ele in freq:
        freq[ele]+= 1
    else:
        freq[ele] = 1
print("occurances of each charcter", freq)

#
# print(b'Easy \xE2\x9C\x85'.decode("utf-8"))

##foudn occurances in list


lst = [1,5,4,1,8,4,1,5,41,1]
di = {}

for ele in lst:
    if ele in di:
        di[ele] =ele +1

    else:
        di[ele]= 1
print("occuraces of list ", di)



###convert list in Discitoray
lst = ["banana", "mango", "apple"]
lst2 = ["yello", "Green", "Red"]

dict1 = dict(zip(lst, lst2))
print(dict1)
