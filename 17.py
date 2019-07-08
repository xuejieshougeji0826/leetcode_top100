class Solution(object):
    def letterCombinations(self, digits):
        dic = {0: 'abc', 1: 'def', 2: 'ghi', 3: 'jkl', 4: 'mno', 5: 'pqrs', 6: 'tuv', 7: 'wxyz'}
        # num=[2,3,4,5,6,7,8,9]
        # char=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        # for i in range(len(num)):
        #     dic[i]=char[i]
        final=[]


s = Solution()
str='23'
print(s.letterCombinations(str))