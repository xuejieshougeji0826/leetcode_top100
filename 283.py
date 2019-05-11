'''给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。'''

class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        a=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                print (nums)
                nums[a]=nums[i]
                print(nums)
                a+=1

        for j in range(a,len(nums)):
            nums[j]=0
        print(nums)

s = Solution()
l = [[0,1,0,3,12]]
print(s.moveZeroes(l))