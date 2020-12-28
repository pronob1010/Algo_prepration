#there has an error
#have to solve it first

def binarySearch_low(list, n):
    first = 0
    last = len(list)-1
    r = 0
    while(first<=last):

        mid = (first + ((last - first) // 2))

        if list[mid] == n:
            r = mid
            last = mid-1

        elif list[mid]<n:
            first = mid+1

        elif list[mid]>n:
            last = mid-1
    return r

def binarySearch_upper(list, n):
    first = 0
    last = len(list)-1
    r = 0
    while(first<=last):

        mid = (first + ((last - first) // 2))

        if list[mid] == n:
            r = mid
            last = mid-1

        elif list[mid]<n:
            first = mid+1

        elif list[mid]>n:
            last = mid-1
    return r

if __name__ == '__main__':
    list = [1,1,2,3,3,3,4,5,6,7,8,9,9,9,9,9,10]
    print(len(list))
    fi = int(input("Find this number :"))
    x = binarySearch_upper(list,fi)
    y = binarySearch_low(list,fi)
    pos = (x-y+1)
    print(x , y)
    print(pos)