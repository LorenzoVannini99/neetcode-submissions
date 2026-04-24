# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Idea
        # question left node and right node recursively
        # each child should return its maximum depth
        # return 1 + max( max_depth(left), max_depth(right) )
        # if a node is a leaf node it should return 1 + max(0, 0) = 1
        # if root is NONE return 0

        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return 1 + max(l, r)   


        
 

        