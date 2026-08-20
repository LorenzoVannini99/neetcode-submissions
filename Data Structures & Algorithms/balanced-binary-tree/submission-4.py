# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            return 1 + max(l,r)    
        
        L = dfs(root.left)
        R = dfs(root.right)

        a = self.isBalanced(root.left) 
        b = self.isBalanced(root.right) 

        if abs(R - L) <= 1 and a and b:
            return True
        else :
            return False 
            




