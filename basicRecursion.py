def fact(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return  n*fact(n-1)

n = int(input())
x = fact(n)
print(x)