class Solution(object):
    def maxCoins(self, nums):
        nums.insert(0,1)
        nums.append(1)
        for i in range(1,nums):
s=Solution()
list=[3,1,5,8]
print(s.maxCoins(list))