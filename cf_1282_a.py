a,b,c,r = list(map(int, input().split()))

if (c>=a) and (c<=b):
    res = ((max(a,b)-min(a,b))-r*2)
    print(res)