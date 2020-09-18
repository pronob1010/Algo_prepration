n = int(input())
for i in range(n):
    stick,diamonds = list(map(int, input().split()))

    def result(min,max):
        if max > (2*min):
            print(min)
        else:
            print((min + max)//3)

    if stick is diamonds:
        max = stick
        min = diamonds
        result(min, max)

    elif stick > diamonds:
        max = stick
        min = diamonds

        result(min, max)

    elif stick < diamonds:
        max = diamonds
        min = stick
        result(min, max)


