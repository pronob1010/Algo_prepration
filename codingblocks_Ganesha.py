n = int(input())

row = n
col = n

print("*", end="")
for i in range(n//2-1):
    print(" ", end="")
print("*", end="")
for i in range(n//2):
    print("*", end="")

print("\n")
for i in range(n//2-1):
    print("*", end="")
    for i in range(n // 2 - 1):
        print(" ", end="")
    print("*", end="")
    print("\n")

for k in range(1,n+1):
    print("*", end="")
print("\n")


for i in range(n//2-1):
    for i in range(n // 2):
        print(" ", end="")
    print("*", end="")
    for i in range(n // 2 - 1):
        print(" ", end="")
    print("*", end="")
    print("\n")


print("*", end="")
for i in range(n//2):
    print("*", end="")

for i in range(n // 2 - 1):
    print(" ", end="")

print("*", end="")