def fun(x):
    if (x > 0):
        x -= 1
        fun(x)
        print(x, end=" ")
        x -= 1
        fun(x)

a = 4
fun(a)



