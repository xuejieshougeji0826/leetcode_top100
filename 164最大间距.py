class Solution:
    def maximumGap(self, nums):
        nums=sorted(nums)
        maxi=0
        for i in range(1,len(nums)):
            maxi=max(maxi,nums[i]-nums[i-1])
        return maxi
s=Solution()
a=[3,1,6,9,90]
print(s.maximumGap(a))
