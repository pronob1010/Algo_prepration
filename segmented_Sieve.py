def sieveoferatosthenes(n):
   primeArray = []
   prime = [True for i in range(n + 1)]
   prime[0] = False

   if n > 0:
      prime[1] = False

   p = 2
   while (p * p <= n):
      if prime[p] == True:
         for i in range(p * 2, n + 1, p):
            prime[i] = False
      p += 1

   for i in range(len(prime)):
      if prime[i] is True:
         primeArray.append(i)
   return primeArray

max = 32000
n = max
p = sieveoferatosthenes(n)
print(p)













