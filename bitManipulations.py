# n = 10
# print("Divition :")
# r = n>>1
# print(r)
# r1 = n>>2
# print(r1)
# r1 = n>>3
# print(r1)
#
# print("Multiplication :")
# r1 = n<<1
# print(r1)
# r1 = n<<2
# print(r1)
# r1 = n<<3
# print(r1)

A = [1,2,3,4,5]
i = 1
while(i<len(A)):
        t = A[i-1]
        A[i-1] = A[i]
        A[i]= t
        i+=2
print(A)