import os

file_size = os.stat("C:\\New folder (2)\\Test.txt")
print((file_size.st_size))
