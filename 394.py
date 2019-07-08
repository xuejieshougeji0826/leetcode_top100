class Solution(object):
    def decodeString(self, s):
        num_stack = []
        char_stack = []
        res = ''
        num_str = ''
        for i in s:
            if i.isdigit():
                # num_stack.append(i)
                num_str += i
            elif i == '[':
                char_stack.append(res)
                num_stack.append(num_str)
                res = ''
                num_str = ''
            elif i == ']':
                res = char_stack.pop() + int(num_stack.pop()) * res
            else:
                res += i
        return res
s = Solution()
str='"2[abc]3[cd]ef"'
print(s.decodeString(list))