def findtwoPoint(li,start,x):
    end = len(li)-1
    # print(li[start])
    while(start<=end):

        if li[start]+li[end]==x:
            # print("f")
            print(li[start],li[end],end=" ")
            return True
        elif li[start]+li[end]<x:
            start += 1
            # print("f2")
        elif li[start] + li[end]>x:
            end -= 1
            # print("f3")
    else:
        return False

def findTriplate(li):
    for i in range(len(li)):
        if findtwoPoint(li,i+1,-(li[i])):
            print(li[i], end=" ")
            return True
    else:
        return False

if __name__=='__main__':
    li = [-3, 3, 1, 7,90,0, -90]
    # x = int(input())
    if findTriplate(li):
        print("\nYes")
    else:
        print("NO")