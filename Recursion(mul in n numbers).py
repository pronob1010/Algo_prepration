# def mulR(n):
#     if n == 1:
#         return 1
#     else:
#         return n*mulR(n-1)
#
# if __name__ == '__main__':
#     print(mulR(int(input())))

def fun1(n):
	i = 0
	if (n > 1):
		fun1(n - 1)
	for i in range(1,n+1):
		print(i,end=" ")
fun1(3)
# This code is contributed by shubhamsingh10
