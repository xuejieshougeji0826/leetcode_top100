class Solution:
    def containsDuplicate(self, nums):
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
s = Solution()
n = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(n))