n,t = list(map(int,input().split()))
a = list(map(int,input().split()))[:n]
c =0
for i in a:
    if i<=t:
        c+=1
        t-=i
print(n-c)

