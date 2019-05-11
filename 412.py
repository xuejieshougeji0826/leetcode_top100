'''写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
示例：
n = 15,
返回:
["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
'''
class Solution:
    def fizzBuzz(self, n: int):
        list=[]
        list2 = []

        for i in range(1,n+1):
            list.append(i)
            list2.append(str(i))
        for j in range(len(list)):
            if list[j]%3==0 and list[j]%5==0:
                list2[j]='FizzBuzz'
            elif list[j]%3==0:
                list2[j] = 'Fizz'
            elif list[j]%5==0:
                list2[j] = 'Buzz'
        return list2

s=Solution()
a=15
print(s.fizzBuzz(a))
