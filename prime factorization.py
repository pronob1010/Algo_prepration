# def SieveOfEratosthenes(n):
#    prime = [True for i in range(n + 1)]
#    p = 2
#    while (p * p <= n):
#       if (prime[p] == True):
#          for i in range(p * 2, n + 1, p):
#             prime[i] = False
#       p += 1
#    prime[0]= False
#    prime[1]= False
#
#    pl = []
#    for p in range(n + 1):
#       if prime[p]:
#          pl.append(p)
#    return pl
#
# x = 100
# p = []
# p= SieveOfEratosthenes(x)
#
# n = int(input())
# t = n
# s = []
# while(t<0):
#     for i in range(len(p)):
#         if p[i]%t==0:
#             s.append(p[i])
#             t = p[i]//t
#             break
# print(s)

import math


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            print(i)
            n = n / i

    if n > 2:
        print(n)


n = 315
primeFactors(n)
