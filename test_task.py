# a,b,c = list(map(int, input().split()))
#
# avg = (a+b+c)//3
# print("Avarage ",avg)
#
# if avg>=1 and avg<=20:
#     for i in range(20):
#         if i == 5:
#             continue
#         elif i == 18:
#             break
#         else:
#             print(i)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # # # a,b,c = list(map(int, input().split()))
# # # #
# # # # avg = (a+b+c)/3
# # # #
# # # # print(avg)
# # # #
# # # # if 1<= avg <= 20:
# # #
# # # # a = 5.5454545
# # # # b= 5.5454545
# # # # print("%.2f %.2f" %(a,b))
# # #
# # # for i in range(8,0,-1):
# # #     if (5 & (1 << i)) != 0:
# # #         print('1', end="")
# # #
# # #     else:
# # #         print('0', end="")
# #
# # m = input()
# # print(type(m))
# # print(type(int(m)))
# #
# # if int(m)%2 == 0:
# #     print("Yes")
# # else:
# #     print("NO")

#
# def binarySearch_low(list, n):
#     first = 0
#     last = len(list)-1
#     r = 0
#     while(first<=last):
#
#         mid = (first + ((last - first) // 2))
#
#         if list[mid] == n:
#             r = mid
#             last = mid-1
#
#         elif list[mid]<n:
#             first = mid+1
#
#         elif list[mid]>n:
#             last = mid-1
#     return r
#
# def binarySearch_upper(list, n):
#     first = 0
#     last = len(list)-1
#     r = 0
#     while(first<=last):
#
#         mid = (first + ((last - first) // 2))
#
#         if list[mid] == n:
#             r = mid
#             last = mid-1
#
#         elif list[mid]<n:
#             first = mid+1
#
#         elif list[mid]>n:
#             last = mid-1
#     return r
#
# if __name__ == '__main__':
#     list = [1,1,2,3,3,3,4,5,6 ,7,8,9,9]
#     fi = int(input("Find this number :")
#
#     f= binarySearch_low(list,fi)
#     l= binarySearch_upper(list,fi)
#
#     print(l-f+1)



# n,k = list(map(int, input().split()))
# s = list(map(int, input().split()))[:n]
#
# selected = s[k-1]
# c = 0
# for i in s:
#     if i!= 0 and i>= selected:
#         c+=1
#
# print(c)

# n = int(input())
# s = list(map(int, input().split()))
# s.sort()
# select = s[0]
# for i in s:
#     if i>select:
#         print(i)
#         break


# from collections import deque
#
# if __name__ == '__main__':
#     n, k = list(map(int, input().split()))
#     nums = list(map(int, input().split()))[:n]
#
#     x = deque(nums)
#     x.rotate(-k)
#     print(*list(x), sep=" ")

# n = int(input())
# s = set()
# for _ in range(n):
#     com, x = list(map(int, input().split()))
#     if com == 1:
#         s.add(x)
#     elif com ==2:
#         s.remove(x)
#     elif com ==3:
#         if x in s:
#             print("Yes")
#         else:
#             print("No")

# t = int(input())
# input()
# for _ in range(t):
#     s = []
#     n = int(input())
#     input()
#     for _ in range(n):
#         s.append(tuple(list(map(int, input().split()))))
#         input()
#     print(*s)


#
# fre = {}
#
# while True:
#     try:
#         num = list(map(int, input().split()))
#         for i in num:
#             if i in fre:
#                 fre[i]+=1
#             else:
#                 fre[i]=1
#
#     except EOFError:
#         break
#
# for key, value in fre.items():
#         print("%d %d"%(key, value))

# from datetime import datetime
# # n = int(input())
# # li = {}
# # for i in range(n):
# #     Name, d,m,y = list(map(str, input().split()))
# #     date_str = m+"-"+d+"-"+y
# #
# #     date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
# #     new = {Name : date_object}
# #     li.update(new)
# #
# # sorted_tuples = sorted(li.items(), key=lambda item: item[1])
# # print(sorted_tuples[len(li)-1][0])
# # print(sorted_tuples[0][0])

#
# def pushleft(li,v,n):
#     if len(li)==n:
#         print("The queue is full")
#     elif len(li) < n:
#         li.insert(0,v)
#         print("Pushed in left: %s"%v)
#     else:
#         print("The queue is empty")
#
#     return li
#
# def pushright(li,v,n):
#     if len(li)==n:
#         print("The queue is full")
#     elif len(li)<n:
#         li.append(v)
#         print("Pushed in right: %s" % v)
#     else:
#         print("The queue is empty")
#
#     return li
#
# def popleft(li):
#     li.pop()
#     print("Popped from left: %s"%v)
#     return li

# def popright(li):
#     li.pop(0)
#     print("Popped from right: %s"%v)
#     return li
#
#
#
#
# t = int(input())
# for i in range(t):
#     n, m = list(map(int, input().split()))
#     li = [][:n]
#     print("Case %d:"%t)
#     for j in range(m):
#         s = input()
#         if " " in s:
#             cmd, v = s.split()
#         else:
#             cmd = s
#
#
#         if cmd == "pushLeft":
#             li = pushleft(li, v,n)
#         elif cmd == "pushRight":
#             li = pushright(li, v,n)
#         elif cmd == "popLeft":
#             li = popleft(li)
#         elif cmd == "popRight":
#             li = popright(li)
#


t = int(input())
input()
for _ in range(t):
    n = int(input())
    input()
    l = []
    for i in range(n):
        a,b = list(map(int, input().split()))
        if i<n-1:
            input()
        l.append([a,b])

    for i in range(len(l)-1):
        for j in range(0, len(l)-1):
            if ((l[j][0]>l[j+1][0]) or ((l[j][0] == l[j+1][0]) and (l[j][1] < l[j+1][1]))):
                l[j], l[j+1] = l[j+1], l[j]

    for i in l:
        print("%d %d"%(i[0], i[1]))
        print()
