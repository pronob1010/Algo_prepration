n,m,a,b = list(map(int,input().split()))
cost = 0
u = b/m

if u<a and n%m == 0:
    cost+= int(u*n)

elif u<a and n%m == 1:
    cost+= int(u*n-1)+a

else:
    cost+= a*n

print(cost)