'''给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3=[]
        jinwei=0

        #str1=l1[0]+l1[1]
        # print (str1)
        # print(l1[0])
        if l1==[]:
            return l2
        elif l2==[]:
            return l1
        else:
            l1 = [l1.val]
            l1 = l1[::-1]
            l2 = [l2.val]
            l2=l2[::-1]
            for i in range(0,min(len(l1),len(l2))):
                if jinwei==0:
                    if l1[i] + l2[i] >= 10:
                        jinwei = 1
                        l3.append(l1[i]+l2[i]-10)
                    else:
                        jinwei = 0
                        l3.append(l1[i] + l2[i])
                elif jinwei==1:
                    if l1[i] + l2[i] +1>= 10:
                        jinwei = 1
                        l3.append(l1[i]+l2[i]-10+1)
                    else:
                        jinwei = 0
                        l3.append(l1[i] + l2[i]+1)
            if len(l1)<len(l2):
                q=len(l2);w=len(l1)
                for k in range(w,q):
                    l3.append(l2[k])
            else:
                q=len(l1);w=len(l2)
                for k in range(w, q):
                    l3.append(l1[k])
            return l3



s = Solution()

#print(s.addTwoNumbers(l1,l2))