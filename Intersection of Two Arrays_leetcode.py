nums1 = [1,2]
nums2 = [1,1]

p = []
if len(nums1)<len(nums2):
    for i in nums1:
        if i in nums2 and i not in p:
            p.append(i)
else:
    for i in nums2:
        if i in nums1 and i not in p:
            p.append(i)

print(p)