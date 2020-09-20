def repeated_digit(n):
    a = []
    # Traversing through each digit
    while n != 0:
        d = n % 10
        # if the digit is present more than once in the number
        if d in a:
            # return 0 if the number has repeated digit
            return 0

        a.append(d)
        n = n // 10

    # return 1 if the number has no repeated digit
    return 1

l=[]
a,b = list(map(int, input().split()))
for i in range(a,b+1):
    n=i
    if repeated_digit(n) is 1:
        l.append(i)

if len(l) > 0:
    print(l[0])
else:
    print('-1')




#--------------------------------

a,b = list(map(int, input().split()))
n_li = []
f = 1
for i in range(a,b+1):
    dig = i
    li = []

    while(dig is not None):
        if dig%10 in li:
            f = 0
            break
        else:
            li.append(dig % 10)

        dig = dig//10

    if f is 1:
        n_li.append(i)

if len(n_li)>0:
    print(n_li[0])
else:
    print('-1')
