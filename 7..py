'''给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例1:

输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max=2**(31 )- 1
        min=-2**31

        rev=0
        if x==0:
            return 0

        elif x>=0:
            while x!=0:
                a=x%10
                rev=rev*10+a
                x=int(x/10)
            if rev>max or rev<min:

                return 0

            else:return rev
        else:
            x=-x
            while x!=0:
                a=x%10
                rev=rev*10+a
                x=int(x/10)
            if -rev > max or -rev < min:
                print('?')

                return 0
            else:return -rev
s = Solution()

print(s.reverse(-232326599216))
