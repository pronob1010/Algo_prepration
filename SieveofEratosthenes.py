def SieveOfEratosthenes(n):
   prime = [True for i in range(n + 1)]
   p = 2
   while (p * p <= n):
      if (prime[p] == True):
         for i in range(p * 2, n + 1, p):
            prime[i] = False
      p += 1
   prime[0]= False
   prime[1]= False

   pl = []
   for p in range(n + 1):
      if prime[p]:
         pl.append(p)
   return pl

n = 164000
p = []
p= SieveOfEratosthenes(n)
for i in range(int(input())):
    n = int(input())
    print(p[n-1])
