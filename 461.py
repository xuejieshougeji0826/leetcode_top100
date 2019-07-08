'''两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
注意：
0 ≤ x, y < 231.
示例:
输入: x = 1, y = 4
输出: 2
解释
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
'''


class Solution:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        a=bin(x^y)
        b=0

        for i in range(len(a)):
            if a[i]=='1':
                b+=1
        return b

s = Solution()
x,y=1,1
print(s.hammingDistance(x,y))