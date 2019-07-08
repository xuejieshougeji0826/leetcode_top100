class Solution:
    def maxSlidingWindow(self, nums, k):
        if len(nums)==0:
            return nums
        else:
            a = []
            for i in range(len(nums)-k+1):
                if i==0:
                    a.append(max(nums[i:i+k]))
                else:
                    if nums[i-1]
            return a



r = Solution()
list1 =[]
b=0
print(r.maxSlidingWindow(list1,b))