t = int(input())
a = list(map(int, input().split()))[:t]

m = max(a)
for i in range(t):
    if a[i] == m:
        break
if i<=3:
    if (i + 1) == 1:
        print("chest")
    elif (i + 1)== 2:
        print("biceps")
    elif (i + 1)== 3:
        print("back")
else:
    if (i + 1) // (3) == 1:
        print("chest")
    elif (i + 1) // (3) == 2:
        print("biceps")
    elif (i + 1) // (3) == 3:
        print("back")

