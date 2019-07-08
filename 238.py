class Solution(object):
    def productExceptSelf(self, nums):
        l=len(nums)
        list_final = []
        list_left=[1,nums[0]]
        list_right=[1,nums[l-1]]
        for i in range(1,l):
            list_left.append(list_left[-1]*nums[i])
            list_right.append(list_right[-1]*nums[l-i-1])
        #list_right.reverse()
        #print(list_right)
        list_final.append(list_right[-2])
        #print(list_final)
        for j in range(1,l):
            list_final.append(list_left[j]*list_right[l-j-1])
        #print(list_final)
        return list_final
s=Solution()
nums=[1,2,3,4]

print(s.productExceptSelf(nums))