nums1 = [0]
nums2 = [1]
m=1
n=1


if len(nums2)>0:
    for i in range(0,len(nums2)):
        nums1.append(nums2[i])

    nums1.sort()
    for i in range(n):
        nums1.remove(0)



print(nums1)