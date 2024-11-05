# def check_string(num):
#   try:
#       float(num)
#       return True
#   except:
#       return False
#
# # n1= 'a'
# # n2 = 1.2
#
# print(check_string('a'))
# print(check_string('1.23'))


def check_int(num):
    try:
        int(num)
        return True
    except:
        return False
print(check_int('1'))
print(check_int("rahul"))
