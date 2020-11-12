import math
def divCount(n):
    i = 1
    c= 0

    while(i*i<=n):
        if i*i== n:
            c+=1
        elif n%i==0:
            c+=2
        i+=1
    return c

n = int(input())
print(divCount(n))