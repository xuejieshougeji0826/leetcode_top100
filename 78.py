
class Solution:
    def subsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        self.helper(res, nums, [])
        return res

    def helper(self, res, nums, re):
        for i in range(0, len(nums)):
            sub = re + [nums[i]]
            res.append(sub)
            print(res)
            self.helper(res, nums[i + 1:], sub)

    def subsets2(self, nums):
        if len(nums) == 0:
            return [[]]
        x = nums.pop(0)
        res = []
        s = self.subsets2(nums)
        for each in s:
            res.append([x]+each)
            res.append(each)
        return res
s=Solution()
a=[1,2,3,4]
print(s.subsets1(a))
#print(s.subsets2(a))
