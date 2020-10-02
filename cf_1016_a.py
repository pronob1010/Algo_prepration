n,m = list(map(int,input().split()))
n1= list(map(int,input().split()))[:n]
c =0
w = 0
for i in n1:
    if i<=m:
        w = m-i
    else:
        c+=1
        w+=i