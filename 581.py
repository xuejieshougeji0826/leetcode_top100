class Solution(object):
    def findUnsortedSubarray(self, nums):
        end=len(nums)
        start=0
        while (end>=start):
            if nums[start]>=nums[start+1]:

s=Solution()
list=[1,2,3,3,3,3]
print(s.findUnsortedSubarray(list))