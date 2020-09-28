# import math
# n = int(input())
# r = math.ceil(math.sqrt(n))
# f =0
# for i in range(2,r):
#     if n%i == 0:
#         f = 1
#         break
# if f == 1:
#     print("No")
# else:
#     print("YES, it's Prime")

# import math
# prime = []
# def simpleSieve(limit):
#     mark = [True for i in range(limit + 1)]
#     p = 2
#
#     while (p * p <= limit):
#         if (mark[p] == True):
#             for i in range(p * p, limit + 1, p):
#                 mark[i] = False
#         p += 1
#
#     for p in range(2, limit):
#         if mark[p]:
#             prime.append(p)
#             print(p, end=" ")

# 2 method's