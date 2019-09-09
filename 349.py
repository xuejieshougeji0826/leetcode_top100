class Solution:
    def intersection(self, nums1, nums2) :
        dic1={}
        for n1 in nums1:
            if not dic1.get(n1):
                dic1[n1]=1
        bingji=[]
        for num in nums2:
            if dic1.get(num):
                bingji.append(num)
                del dic1[num]
        return  bingji
r = Solution()
list1=[1,2,2,1]
list2=[2,2]
print(r.intersection(list1,list2))
