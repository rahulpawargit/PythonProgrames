def check_finelen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print(check_finelen("C:\\New folder (2)\\Test.txt"))