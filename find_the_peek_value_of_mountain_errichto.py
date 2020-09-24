a = [2,3,4,5,6,7,8,9,12,11,8,6,4,1,2,3,4,5,6,7,8,9,9,13,12,11,8,6]

first = 0
last = len(a)-1

while(first<= last):
    mid = first + (last-first)//2

    if a[mid]>a[mid-1]:
        print(a[mid])
        ans = mid
        first = mid+1

    elif a[mid]<a[mid-1]:
        last = mid-1
print(ans)

