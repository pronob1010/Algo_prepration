#Fibonacci series

def fibbo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        x = fibbo(i)
        print(x)