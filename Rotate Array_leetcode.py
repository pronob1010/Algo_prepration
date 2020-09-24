nums = [1,2,3,4,5,6,7]
k = 3


for i in range(k):
    previous = nums[-1]
    for j in range(len(nums)):
        temp = nums[j]

        # nums[j], previous = previous, nums[j]

        nums[j] = previous
        previous = temp
    print(nums)
    print("----------")
print(nums)




