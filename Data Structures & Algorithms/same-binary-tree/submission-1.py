# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Recursion:
        # at each step
        # if p and not q or q and not p --> return False
        # if p.val != q.val --> return False
        # if isSameTree(p.left) == isSameTree(q.left) and
        # isSameTree(p.right) == isSameTree(q.right) return True else False

        if not p and not q :
            return True

        if p and not q or q and not p:
            return False

        if p.val != q.val:
            return False

        bool_left = self.isSameTree(p.left, q.left)
        bool_right = self.isSameTree(p.right, q.right)

        return bool_left and bool_right     





 

        