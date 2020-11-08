#works for unick values

def binarySearch(list):
    first = 0
    N = len(list)
    last = N-1

    while(first<=last):
        mid = (first + (last-first)//2)

        prev = (mid+N-1)% N #this use to prevent index error
        next = (mid+1)% N #this use to prevent index error

        if list[prev]>=list[mid] and list[mid]<=list[next]:
            return mid

        elif list[first] <= list[mid]:
            first = mid+1

        elif list[last] > list[mid]:
            last = mid-1
if __name__ == '__main__':
    list = [12, 15, 11]
    x = binarySearch(list)
    if x == None:
        print(0)
    else:
        print(len(list)-x)