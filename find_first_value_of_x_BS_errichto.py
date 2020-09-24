a = [1,2,3,6,7,9]
x = 8
store = 0
first = 0
last = len(a)-1

while(first<=last):

    mid = first + (last-first)//2

    if a[mid]>=x:
        store = a[mid]
        last = mid-1

    elif a[mid]<x:
        first = mid +1

print(store)

