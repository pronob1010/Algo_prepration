nums = [1,2,3,4,5,6,7]
k = 3

#approch1
for i in range(k):
    previous = nums[-1]
    for j in range(len(nums)):
        temp = nums[j]
        nums[j] = previous
        previous = temp
        # nums[j], previous = previous, nums[j]
    print(nums)
    print("----------")

#approch2
#
# n = len(nums)
# a = [0] * n
# for i in range(n):
#     a[(i + k) % n] = nums[i]
#
# nums[:] = a


print(nums)




