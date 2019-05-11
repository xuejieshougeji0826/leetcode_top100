class Solution:
    def findKthLargest(self, nums,k):
        nums=sorted(nums)
        print(nums)
        return nums[len(nums)-k]

s = Solution()
a = [3,2,1,5,6,4]
l=2
print(s.findKthLargest(a,l))
