class Solution:
    def findMedianSortedArrays(self, nums1,nums2):
        i=0;j=0;
        l1=len(nums1)
        l2=len(nums2)
        nums3=[]
        while (i!=l1 or j!=l2):
            if  i >= l1 or j >= l2 :
                return nums3
            else:
                if(nums1[i]<=nums2[j]):
                    try:
                        nums3.append(nums1[i])
                        i+=1
                        print(nums3)
                    except:
                        nums3.append(nums2[j])
                        j+=1
                        print(nums3)
        print(nums3)
s = Solution()
a = [1, 2]
b=[0,4]
print(s.findMedianSortedArrays(a,b))


