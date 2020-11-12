import math
def seiveoferatothenis(n):
    primebool = [True]*(n+1)
    primebool[0]= False
    primebool[1]=False
    i = 2
    while(i*i<=n):
        if primebool[i] == True:
            for i in range(i*2,n+1,i):
                primebool[i]=False
        i+=1
        prime = []
        for i in range(n+1):
            if primebool[i]== True:
                prime.append(i)

    return prime

def primefactor(x):
    p = []
    n = math.ceil(math.sqrt(x))
    p = seiveoferatothenis(n+1)
    fact = []
    i = 0
    f = 0
    t = x

    while(i<len(p)):
        if (p[i]<=x):
        # print("y")
            if (x % p[i] == 0):
                f = 1
                fact.append(p[i])
                x = x // p[i]
        if f == 0:
            i+=1
        else:
            i = 0
            f = 0

    if x != 1:
        fact.append(t)
    return fact

if __name__=="__main__":
    x = int(input())
    fact= []
    fact = primefactor(x)
    f = {}
    for i in fact:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    c = 1
    for i in f.values():
        c*=i+1
    print(c)