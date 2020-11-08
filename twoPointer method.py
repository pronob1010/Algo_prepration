def twoPointer(li,x):
    l = 0
    r = len(li)-1
    while(l<=r):
        if li[l]+li[r] == x:
            return True
        elif li[l]+li[r]<x:
            l+=1
        elif li[l]+li[r] >x:
            r-=1
    else:
        return False

if __name__=='__main__':
    li = [-1,3,0,4,6,7]
    li.sort()
    x = int(input("Enter the value that you want to divide by array:"))
    if twoPointer(li, x):
        print("Found")
    else:
        print("Not Found")
