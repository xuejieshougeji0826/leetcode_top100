# class Solution:
#     def minPathSum(self, grid):
#         m = len(grid)
#         if m < 1:
#             return 0
#         n = len(grid[0])
#         if n < 1:
#             return 0
#         dp = []
#         for i in range(m):
#             dp.append([0]*n)
#         dp[0][0] = grid[0][0]
#         for i in range(1,n):
#             # 第一行
#             dp[0][i] = grid[0][i] + dp[0][i-1]
#         for i in range(1,m):
#             dp[i][0] = grid[i][0] + dp[i-1][0]
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
#         return dp[m-1][n-1]
#

class Solution:

    # 动态规划
    def minWay(self, grid, m, n):
        memo = [([0] * n) for i in range(m)]
        memo[0][0] = grid[0][0]
        # 应该先算两边的，因为只有一种情况
        for i in range(1, m):
            memo[i][0] = memo[i-1][0]+grid[i][0]
            # print(memo[0])
            # print(memo[1])
            # print(memo[2])
        for j in range(1, n):
            memo[0][j] = memo[0][j-1]+grid[0][j]
            # print(memo[0])
            # print(memo[1])
            # print(memo[2])

        for i in range(1,m):
            for j in range(1,n):
                memo[i][j] = min(memo[i][j-1]+grid[i][j],memo[i-1][j]+grid[i][j])
                print(memo[0])
                print(memo[1])
                print(memo[2])
                print(' ')
        return memo[m-1][n-1]
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0]) #mxn的网格
        return self.minWay(grid, m, n)
s=Solution()
a=[[1, 3, 1],[1, 5, 1],[4, 2, 1]]

print(s.minPathSum(a))
