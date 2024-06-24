import random as rd

def listAlphabet():return [chr(i) for i in range(ord("a"), ord("z") + 1)]

for b in range(0,1):
    for a in range(0,4):
        for i in range(0,6):
            if rd.randint(1,3) != 1:
                if rd.randint(1,2) != 1:print(str(rd.choice(listAlphabet())), end="")
                else:print(str(rd.choice(listAlphabet()).upper()), end="")
            else:print(str(rd.randint(0,9)), end="")
        print(" ", end="")    
    print(" ")