#Anagrame means sortign words it will create new word

str1 = 'race'
str2 = "care"

str1= str1.lower()
str2 = str2.lower()

if (len(str1)== len (str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1==sorted_str2:
        print(str1, 'and', str2, 'are anogram')
    else:
        print("Strings are not anogram")
else:
    print("Strings are not anogram")





