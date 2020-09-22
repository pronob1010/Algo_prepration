n = input()
x = n
c =0
for i in range(len(n)):
    if n[i] is '.':
        for j in range(i+1,len(n)):
            c+=1
        break
print(c)


#not complited