'''给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        m=0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    print (i,j)
                    m=max(m,j-i+1)
        return(m)
s = Solution()
s1="abcabcbb"
print(s.lengthOfLongestSubstring(s1))



