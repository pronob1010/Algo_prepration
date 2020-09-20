n = int(input())
el = list(map(int,input().strip().split()))[:n]

mx = []

for i in range(len(el)):
    for j in range(len(el)):
        if not(el[i] == el[j]):
            mx.append(el[i]*el[j])

print(max(mx))
