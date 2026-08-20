# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Idea :
        # Use recursion
        # at a particular node i, we return height from the left and right
        # then recursively call dfs
        # if they differ by no more than 1 return True
        # 
        # TC : O(n)
        # SC : O( log(n) ) if balanced
        #

        if not root :
            return True
        
        def depth(root):

            if not root :
                return 0

            return 1 + max( depth(root.left), depth(root.right) )    
        
        if root.left:
            l = depth(root.left)
            bool_left = self.isBalanced(root.left)
        else :
            l = 0
            bool_left = True

        if root.right:    
            r = depth(root.right)
            bool_right = self.isBalanced(root.right)
        else :
            r = 0
            bool_right = True
        
        if ( abs ( l - r) <= 1 and bool_right and bool_left ):
            return True
        else :
            return False    




