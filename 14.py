'''编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。'''
class Solution:
    def longestCommonPrefix(self, strs):
        class Solution(object):
            def longestCommonPrefix(self, strs):
                """
                :type strs: List[str]
                :rtype: str
                """
                if not strs:
                    return ''
                dp = [strs[0]] * len(strs)
                for i in range(1, len(strs)):
                    while not strs[i].startswith(dp[i - 1]):
                        dp[i - 1] = dp[i - 1][:-1]
                    dp[i] = dp[i - 1]
                return dp[-1]


s=Solution()
l=["flower","flow","flight"]
print(s.longestCommonPrefix(l))
