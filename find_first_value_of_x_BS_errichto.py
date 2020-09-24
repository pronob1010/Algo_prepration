a = [1,2,3,6,7,8,9]
x = 4
store = []
first = 0
last = len(a)-1

while(first<=last):

    mid = first + (last-first)//2

    if a[mid]>=x:
        store.append(a[mid])
        last = mid-1

    elif a[mid]<x:
        first = mid +1

print(min(store))

