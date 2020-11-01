def mulR(n):
    if n == 1:
        return 1
    else:
        return n*mulR(n-1)

if __name__ == '__main__':
    print(mulR(int(input())))