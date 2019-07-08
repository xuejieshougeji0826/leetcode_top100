class Solution(object):
    def topKFrequent(self, nums, k):
        final=[]
        dic={}
        for j in range(len(nums)):
            dic[nums[j]]=0
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return nums
        else:
            for i in range(len(nums)):
                dic[nums[i]] +=1
        dics=sorted(dic.items(), key=lambda obj: obj[1])
        print(dics)
        for z in range(0,k):
            final.append(dics[len(dics)-z-1][0])

        return final


s=Solution()
list=[1,1,1,2,2,3]

a=2
print(s.topKFrequent(list,a))