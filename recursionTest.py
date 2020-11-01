# #test -1
# def fun(x):
#     if (x > 0):
#         x -= 1
#         fun(x)
#         print(x, end=" ")
#         x -= 1
#         fun(x)
#
# a = 4
# fun(a)
#
##test -2

def fun(n):
    if n%2==0:
        n+=1
        return n
    else:
        return fun(fun(n-1))
if __name__ == '__main__':
    n = 200
    print(fun(n))