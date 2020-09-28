t = int(input())
for i in range(t):
    n = int(input())
    # for i in range(n):
    #     if(pow(2,i))<n:
    #         k = pow(2,i)
    #
    # r = 1 + (n-k)
    # print(r)
    # r = 0
    c = 0
    bi = str(bin(n))

    for i in range(len(bi)):
        # print(bi[i])
        if bi[i] == '1':
            c +=1
    print(c)