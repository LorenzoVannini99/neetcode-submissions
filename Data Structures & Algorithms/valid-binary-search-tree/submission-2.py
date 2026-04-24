# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Idea :
        # pass root, min and max as function arguments
        # Whenever we turn right, i should update the minimum <-- root.val
        # Whenever we turn left, i should update the maximum <-- root.val
        
        m = - 10000000
        M = - m

        if not root.left and not root.right :
            return True
        
        def dfs(root, minimum = m, maximum = M):
            if not root :
                return True

            if not ( minimum < root.val < maximum ):
                return False
            
            L = dfs ( root.left, minimum = minimum, maximum = root.val)
            R = dfs ( root.right, minimum = root.val, maximum = maximum)

            return L and R

        return dfs(root)    

        
                        

 







        