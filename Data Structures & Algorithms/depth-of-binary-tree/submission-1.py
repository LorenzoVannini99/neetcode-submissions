# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Idea :
        # Use recursion
        # at a particular node i, we take the depth from the left and right node
        # so the return is max ( left_depth, right_depth) + 1
        # then recursively call dfs
        # TC : O(n)
        # SC : O( log(n) ) if balanced
        #

        if not root :
            return 0
        
        if root.left:
            l = self.maxDepth(root.left)
        else:
            l = 0

        if root.right:
            r = self.maxDepth(root.right)
        else :
            r = 0       
        
        return 1 + max(l,r) 

        
 

        