a = [2,3,4,5,6,7]

val = 34
pos =  0
temp = 0
for i in range(pos,len(a)):
    if i>= pos:
        temp = int(a[i])
        a[i]=val
        val=temp

a.append(temp)
print(a)