def removeDuplicates(List):
    n = len(List)
    c_i = 1
    for i in range(1, n):
        if List[i - 1] != List[i]:
            List[c_i] = List[i]
            c_i += 1
    return c_i

n = [1,1,2,2,3]
print(n[:removeDuplicates(n)])

# p = []
# for i in n:
#     if i not in p:
#         p.append(i)
#
# n = list(set(n))
# print(n)