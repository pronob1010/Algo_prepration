a ,b,c = list(map(int,input().split()))
p=a
r =a
i = 1
while True:
    if (c is p) or ( c is r):
        print("YES")
        break

    if r > c or p>c :
        print("No")
        break

    p = a + i * b
    r = a + i * b + 1
    i+=1