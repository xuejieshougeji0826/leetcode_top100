class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        a=float('-inf')

        if len(nums)==0:
            return 0
        else:
            for i in range(0,len(nums)):
                print ('i='+str(i))
                sum=0
                for j in range(i,len(nums)):
                    sum=sum+nums[j]
                    print(sum)
                    a=max(sum,a)
                    print (a)
            return a
s=Solution()
q=[-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(q))