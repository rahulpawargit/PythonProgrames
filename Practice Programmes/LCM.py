# LCM- Least Comment Multiplier

def lcm(x, y):
    if x > y :
        greatest = x
    else:
        greatest = y

    while(True):
        if (greatest % x == 0) and (greatest % y == 0):
            leastNo= greatest
            break
        greatest += 1
    return leastNo


n1= 57
n2 = 24

print("Least comment multiplier", lcm(n1,n2))