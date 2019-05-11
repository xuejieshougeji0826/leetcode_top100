'''给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        return s.just(root.left,root.right)
    def just(self,l,r):
        if not l or not r:
            if not l and not r:
                return True
            else:return False
        if l.val==r.val:

            return s.just(l.right,r.left) and s.just(l.left,r.right)
        else: return False


s=Solution()
