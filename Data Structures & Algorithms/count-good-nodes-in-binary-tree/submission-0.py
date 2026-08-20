# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maximum = -101) : 
            
            if not node :
                return 0

            if node.val >= maximum:
                res = 1
                maximum = node.val
            else :
                res = 0

            res = res + dfs(node.left,maximum)
            res = res + dfs(node.right,maximum)        

            return res
        
        return dfs(root)
            

