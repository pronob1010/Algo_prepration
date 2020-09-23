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