# leetcode_w1_t2
def f(n):
    sum = 0
    while (n):
        digit = n % 10
        n = n // 10
        sum += digit * digit
    return sum


def isHappy(n):
    pp = []
    r = f(n)
    while (r != 1):
        r = f(n)
        n = r
        if n in pp:
            return False
        pp.append(n)
    return True

n  = int(input())
print(isHappy(n))