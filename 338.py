class Solution:
    def countBits(self, num):
        lll=[]
        for i in range(num):
            lll.append(i&(i-1)+1)
        return lll

r=Solution()
list1=5
print(r.countBits(list1))
