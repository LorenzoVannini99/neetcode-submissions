# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lower = -1001, upper = + 1001) :

            if not node :
                return True
            
            if not lower < node.val < upper :
                return False
            
            if node.left :
                if node.left.val > node.val :
                    return False

            if node.right :
                if node.right.val < node.val :
                    return False

            l = dfs ( node = node.left, lower = lower, upper = node.val )
            r = dfs ( node = node.right, lower = node.val, upper = upper )

            if l and r :
                return True
            
            return False

        return dfs(root)       
        


            
         




        