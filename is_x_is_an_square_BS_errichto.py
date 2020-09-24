n = int(input())
f = 0

div = n//2
first = 1
last = div
while(first<=last):
    mid = first+(last-first)//2
    if mid*mid == n:
        print('YES')
        f =1
        break
    elif(mid*mid < n):
        first = mid+1
    else:
        last = mid - 1
if f == 0:
    print('NO')

