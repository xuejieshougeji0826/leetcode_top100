'''给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true'''


class Solution:
    def isValid(self, s):
        list=[]
        left=['[','{','[']
        l=len(s)
        if l<0:
            return False
        elif l==0:
            return True
        else:
            list.append(s[0])
        for i in range(1,l):
            if list==[]:
                list.append(s[i])
            elif s[i]=='}' and list[-1]=='{':
                list.pop()
            elif s[i]==')' and list[-1]=='(':
                list.pop()
            elif s[i] == ']' and list[-1] == '[':
                list.pop()
            else:list.append(s[i])
            #print(list)
        if list==[]:
            return True
        else:return False






s = Solution()
list =[]
print(s.isValid(list))
# for j in range(len(list)):
#     list.pop()
#     print(list)

