# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

new_str = [i.lower() for i in my_str.split()]

new_str.sort()
# my_str.sort()

print(new_str)
# for i in new_str:
#     print(i)