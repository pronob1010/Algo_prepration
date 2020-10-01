n = int(input())
f = 0
temp = []
temp.append(n % 10)
if (n != 1444) and (n != 514) and (n != 414):
    while n != 0:
        r = n % 10
        if (r == 1 or r == 4):
            if r== 4 and temp[len(temp)-1] ==r:
                break
            f = 1
        else:
            f = 0
            break
        n = n // 10

    if f == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
