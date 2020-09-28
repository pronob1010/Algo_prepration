import math
n = int(input())

r = math.ceil(math.sqrt(n))
f =0
for i in range(2,r):
    if n%i == 0:
        f = 1
        break
if f == 1:
    print("No")
else:
    print("YES, it's Prime")