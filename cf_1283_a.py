t = int(input())
for _ in range(t):
    h,m = list(map(int,input().split()))

    h = 24 - h
    m = 60 - m
    if h is 1:
        print(m)
    else:
        r = (h*60) + m
        print(r)