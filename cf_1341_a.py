t = int(input())
for i in range(t):
    n,a,b,c,d = list(map(int, input().split()))

    if ((c-d) <=(n*(a-b)) <=(c+d)):
        print('Yes')
    elif ((c-d)<= (n*(a+b)) <= (c+d)):
        print('Yes')
    else:
        print('No')

