class Solution:
    def maxProfit(self, prices):
        maxs=0
        minx=0
        for i in range(len(prices)):
            min_price=min(prices[i],minx)
            max_price=max(prices[i]-min_price,maxs)
        return max_price

s = Solution()
a = [7,1,5,3,6,4]
print(s.maxProfit(a))
