#Anagrame means sortign words it will create new word

str1 = 'race'
str2 = "care"

str1= str1.lower()
str2 = str2.lower()

# if (len(str1)== len (str2)):
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
#
#     if sorted_str1==sorted_str2:
#         print(str1, 'and', str2, 'are anogram')
#     else:
#         print("Strings are not anogram")
# else:
#     print("Strings are not anogram")


if len(str1)==len(str2):
    sortedstr1 = sorted(str1)
    sortedstr2= sorted(str2)

    if sortedstr1 == sortedstr2:
        print("Strings are sorted")
    else:
        print("Striing are not sorted")
else:
    print("strings are not sorted")




