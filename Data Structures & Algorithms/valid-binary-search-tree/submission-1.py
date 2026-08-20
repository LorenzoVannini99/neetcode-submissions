# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Idea :
        # Recursively thinking about node i 
        # is BST if left is BST and right is BST
        # if node.left is avaiable and node.left.val > node return False
        # else, update upper limit
        # if node.right is avaiable and node.right.val < node return False
        # else, update lower limit
        # for the first root, l = -inf, u = inf
        # TC : O(n)
        # SC : O ( h ) on average O ( logn )
        
        def dfs(root, l = float("-inf"), u = float("inf")):

            if not root :
                return True

            if not ( l < root.val < u):
                return False

            left = dfs(root.left, l = l, u = root.val)
            right = dfs(root.right, l = root.val, u = u)   

            return left and right    
        
        return dfs(root)
        


            
         




        