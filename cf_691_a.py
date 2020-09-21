li = []
n = int(input())
s = list(map(int,input().strip().split()))[:n]
li = [int(i) for i in s]
li.reverse()
f = 0

for i in range(len(li)):
    if s[i] is li[i]:
        f = 0
    else:
        f = 1
        break

if f is 0:
    print('YES')
else:
    print('NO')
