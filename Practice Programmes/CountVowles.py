
vowles = "aeiou"

str1= ("This is a my first string ou")


count = {}.fromkeys(vowles,0)
for char in str1:
    if char in count:
        count[char] +=1
print(count)
