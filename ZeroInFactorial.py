n = int(input())
p=5
r=0
i=1
pr = pow(p,i)
z = (n//pr)
while(z>0):
    pr = pow(p,i)
    z = (n // pr)
    r += z
    i+=1
print(r)