'''假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''
#第一个方法超时间了

# class Solution:
#     def climbStairs(self, n: 'int') -> 'int':
#         if n==1:
#             return 1
#         elif n==2:
#             return 2
#         else:
#             sums=s.climbStairs(n-1)+s.climbStairs(n-2)
#         return sums

class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        arr=[1,2]
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            for i in range (2,n):
                add=arr[len(arr)-1]+arr[len(arr)-2]
                arr.append(add)
                # print (arr)
        return arr[len(arr)-1]



s = Solution()

print(s.climbStairs(6))
