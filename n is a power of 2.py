n = int(input())

#normal way
# if n==0:
#     print("No")
# else:
#     while(n%2==0):
#         n/=2
#     if n== 1:
#         print("Yes")
#     else:
#         print("NO")

#optimized way

r = n&(n-1)
if r== 0:
    print("Yes")
else:
    print("NO")
