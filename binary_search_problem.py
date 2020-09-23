# a = [2,3,4,6,9,12,11,8,6,4,1]
# #find the maximun??
# max = a[0]
# l = 0
# r = len(a)
# while(l<r):
#     mid = l + (r-l)/2 #same as (l+r)/2
#
#     if a[mid]>max:
#         max = a[mid]
#     else:

class Solution:
    def singleNumber(self, List):
        fre = {}
        for i in List:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1

        return min(fre, key= lambda x: fre[x])


List=[4,1,2,1,2]
myobj = Solution()
print(myobj.singleNumber(List))

#
# def List( List):
#     l = []
#     for i in range(len(List)):
#         if List[i] not in l:
#             l.append(List[i])
#
#     print(l)
#
# List=[2,2,1]
#
# print(singleNumber(List))