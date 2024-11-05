puchuations= "!@#$%^&*()_,:?>?....<"

str1= "Hello, ! How are you ??..."

no_puch= ""

for char in str1:
    if char not in puchuations:
        no_puch= no_puch + char

print(no_puch)