nums = [1,2,3,4,5,6,7]
k = 3
# o = []
#
# for i in range(0,len(nums)-k):
#     o.append(nums[i])
#     del(nums[i])
#
# print(o)
# print(o+nums)
print(nums[k:])
print(nums[k+1:]+nums[:k+1])