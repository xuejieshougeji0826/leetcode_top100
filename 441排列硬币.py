# class Solution:
#     def arrangeCoins(self, n):
#         def sum(l):
#             return (l*(l+1))/2
#         i=0
#         if n==1:
#             return 1
#         elif n==0:
#             return 0
#         else:
#             while(sum(i)<=n):
#                 i+=1
#
#             return i-1
class Solution:
    def arrangeCoins(self, n):
        num=int((2*n)**0.5)
        if n<=1:
            return n
        else:
            if (num*(num+1)*0.5)<=n:
                #print(num)
                return num
            else:return num-1

s = Solution()
a = 3
print(s.arrangeCoins(a))
