def binarySearch(list, n):
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

if __name__=='__main__':

    list = [1,1,2,3,3,3,4,5,6 ,7,8,9,9]

    print(len(list))
    f=int(input("Find this number :"))
    r = binarySearch(list, f)
    print(r)