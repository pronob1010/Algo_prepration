n = [2,2,1]
p = {}

for i in n:
    if i in p:
        p[i] +=1
    else:
        p[i] = 1

s_n = min(p, key=lambda x:p[x])
print(s_n)