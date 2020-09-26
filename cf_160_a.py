n = int(input())
s = list(map(int, input().split()))[:n]

se = {}
for i in s:
    if i in se:
        se[i] += 1
    else:
        se[i] = 1

print(se.values())
if len(s)>1:
    r = [int(i) for i in se.values() if(i == 2)]
    print(sum(r))
else:
    print('1')

