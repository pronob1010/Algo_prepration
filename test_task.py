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
    list = [1,1,2,3,3,3,4,5,6 ,7,8,9,9]
    fi = int(input("Find this number :")

    f= binarySearch_low(list,fi)
    l= binarySearch_upper(list,fi)

    print(l-f+1)