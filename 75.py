class Solution:
    def sortColors(self, nums):
        a1=0
        a2=0
        a3=0
        l=len(nums)
        for i in range(l):
            if nums[i]==0:
                a1+=1
            elif nums[i]==1:
                a2+=1
            else:a3+=1
        for i in range(a1):
            nums[i]=0
        for i in range(a2):
            nums[a1+i]=1
        for i in range(a3):
            nums[a1+a2+i]=2



r = Solution()
list1 = [1,1,0,2,1,0,2,1]
print(r.sortColors(list1))