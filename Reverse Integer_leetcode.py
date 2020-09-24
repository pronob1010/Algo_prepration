def sss(x):
    if x!= 0:
        p=[]
        s = x
        s= abs(s)
        while(s!=0):
            if len(p) == 0 and s%10 == 0:
                pass
            else:
                p.append(s%10)
            s = s//10

        l = ''.join([str(elem) for elem in p])

        if int(l)>(2**31-1):
            return 0
        if x<0:
            l='-'+l

        return l
    else:
        return 0
x = 1534236469
print(sss(x))

