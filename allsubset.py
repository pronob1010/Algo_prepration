import math

def subset(list,size):
    new_size = int(math.pow(2,size))

    for counter in range(0,new_size):
        for j in range(0,size):
            if ((counter & (1<<j))>0):
                print(list[j],end="")
        print()



list = ['a','b','c']
l = len(list)

subset(list,l)
