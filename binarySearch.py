def binarySearch(list,f):
    start = 0
    end = len(list)-1
    while(start<=end):
        mid = (start + (end-start) // 2)

        if list[mid] is f:
            return f

        elif list[mid]> f:
            end = mid-1

        elif list[mid]< f:
            start = mid+1


list = [1,2,3,4,5,6 ,7,8,9]
f=int(input("Find this number :"))

r = binarySearch(list,f)
if r is -1:
    print("Not found")
else:
    print(r)