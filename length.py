import random

name = "Eric Wright"
length = len(name)
print(name,"has",length,"characters")
indexPos = random.randrange(0,length)
char = name[indexPos]
print(char)
if indexPos <= length:
    char = name[indexPos]
else:
    print("that wont work")