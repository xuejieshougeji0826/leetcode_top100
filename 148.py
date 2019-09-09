# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def sortList(self, head: ListNode) -> ListNode:



r = Solution()
list=[4,2,1,3]
# 遍历链表
def travel_listnode(head):
    res = head
    while res is not None:
        print(res.val)
        res = res.next

        # 将列表转换成链表
def list_to_listnode(numbers):
    dummy_root = ListNode(0)
    # print(dummy_root)
    # print(ListNode(0))
    #travel_listnode(dummy_root)
    ptr = dummy_root
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
        travel_listnode(dummy_root)
        print('\n')
    ptr = dummy_root.next
    return ptr

travel_listnode(list_to_listnode(list))
