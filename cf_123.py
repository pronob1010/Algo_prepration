# def Fibonacci(n):
# 	if n==1:
# 		return 0
# 	elif n==2:
# 		return 1
# 	else:
# 		return Fibonacci(n-1)+Fibonacci(n-2)
def Fibonacci(n):
   if n <= 1:
       return n
   else:
       return(Fibonacci(n-1) + Fibonacci(n-2))

n = int(input())
sum = 0

for i in range(1,n+1):
  sum +=Fibonacci(i)
print(sum)


