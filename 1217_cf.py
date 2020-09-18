# def binarySearch( stre, inte, exp):
#     start = 1
#     end = exp
#     f=0
#
#     while(stre+start) >= inte + (exp-start):
#         mid = (start + end) // 2
#
#         if (stre+start) > inte + (exp-start):
#             f += 1
#             return f
#
#         elif (stre+start) <= inte + (exp-start):
#             start = mid + 1

for k in range(int(input())):
    stre, inte, exp = list(map(int, input().split()))
    list = []
    list = [int(i) for i in range(1,exp+1)]

    # r = binarySearch( stre, inte, exp)
    # print(r)

    c = 0
    for i in range(len(list)):
        if (stre + list[i]) > (inte + (exp-list[i])):
            print((stre + list[i]),(inte + (exp-i)))
            c += 1

    print(c)
    list = []
    print(list)
