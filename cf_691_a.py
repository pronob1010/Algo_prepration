li = []
n = int(input())
s = list(map(int,input().strip().split()))[:n]
# li = [int(i) for i in s]
# li.reverse()
f = 0

for i in range(len(s)):
    if s[i] is 1:
        li.append(s[i])


if len(li)>1:
    print('YES')
else:
    print('NO')
