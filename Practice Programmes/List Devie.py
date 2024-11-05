#slip list in Evently sized

def split_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst [i:i + size]

size = 3
lst=[1,2,5,4,8,6,5,1,4,7,2]
print(list(split_list(lst, size)))