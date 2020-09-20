# n = int(input())
# el = list(map(str,input().strip().split()))[:n]
#
# print(el)
#
# mx = []
#
# for i in len(el):
#     for j in len(el):
#         if int(el[i]) is int(el[j]):
#             continue
#         else:
#             mx.append(int(el[i])*int(el[j]))
#
# print(max(mx))
#
#
# #unsolveddddddddddddd

a,b = list(map(int, input().split()))
n_li = []
f = 1
for i in range(a,b+1):
    f = 1
    dig = i
    li = []

    while(dig is not None):
        if dig%10 in li:
            f = 0
            break

        li.append(dig % 10)
        dig = dig//10

    if f is 1:
        n_li.append(i)



if len(n_li)>0:
    print(n_li[0])
else:
    print('-1')
