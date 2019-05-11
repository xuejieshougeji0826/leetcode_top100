class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            x1=x
            
            for i in range(int(len(str(x))/2)):
                temp=x[i]
                x[i]=x[len(x)-1-i]
                x[len(x) - 1 - i]=temp
            if x1==x:
                return True
            else:
                return False

s = Solution()
a = int(121)
print(s.isPalindrome(a))
