t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    c = list(map(int, input().split()))[:n]
    p = []
    f = 0
    f1 = 0
    f2 = 0

    for j in range(1,n):
        if (f==0) and (a[j-1] == a[j]):
            f = 1
            l = len(p)
            if l>n:
                p.append(a[j - 1])
            else:
                break

        elif (a[j-1] != a[j]):
            p.append(a[j - 1])

    print(p)

    # for j in range(1,n):
    #     if (f==0) and (a[j-1] == a[j]):
    #         f = 1
    #         l = len(p)
    #         if l>0 and p[l-1]!=a[j-1]:
    #             p.append(a[j - 1])
    #         else:
    #             p.append(a[j-1])
    #
    #     elif (a[j-1] != a[j]):
    #         l = len(p)
    #         if l > 0 and p[l - 1] != a[j - 1]:
    #             p.append(a[j - 1])
    #         else:
    #             p.append(a[j - 1])
    # print(p)
    #
    # for j in range(1,n):
    #     if (f1==0) and (b[j-1] == b[j]):
    #         f1 = 1
    #
    #         l = len(p)
    #         if l > 0 and p[l - 1] != b[j - 1]:
    #             p.append(b[j - 1])
    #         else:
    #             p.append(b[j - 1])
    #
    #     elif (b[j-1] != b[j]):
    #         l = len(p)
    #         if l > 0 and p[l - 1] != b[j - 1]:
    #             p.append(b[j - 1])
    #         else:
    #             p.append(b[j - 1])
    # print(p)
    #
    # for j in range(1,n):
    #     if (f2 == 0) and (c[j-1] == c[j]):
    #         f2 = 1
    #         l = len(p)
    #         if l > 0 and p[l - 1] != c[j - 1]:
    #             p.append(c[j - 1])
    #         else:
    #             p.append(c[j - 1])
    #     elif (c[j-1] != c[j]):
    #         l = len(p)
    #
    #         if l > 0 and p[l - 1] != c[j - 1]:
    #             p.append(c[j - 1])
    #         else:
    #             p.append(c[j - 1])
    # print(p)