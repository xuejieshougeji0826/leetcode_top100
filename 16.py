class Solution:
    def threeSumClosest(self, nums, target):
        nums=sorted(nums)
        ttt=[]
        min_chazhi=[]
        for i in range(1,len(nums)-1):
            sum=nums[i-1]+nums[i]+nums[i+1]
            min_chazhi.append(sum)
            ttt.append(abs(target-sum))
        print(min_chazhi)
        print(ttt)
        nums_final=min(ttt)
        position=ttt.index(nums_final)
        return min_chazhi[position]
s = Solution()
a =[0,2,1,-3]
b=1
print(s.threeSumClosest(a,b))
