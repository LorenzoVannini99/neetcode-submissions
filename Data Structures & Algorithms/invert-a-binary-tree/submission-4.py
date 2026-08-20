# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Think about each layer, each node
# for each layer, swap left and right
# if it is none, well you have reached a leaf --> do nothing
# TC : O(n) --> well I must visit the entire tree
# SC : O(h) --> how many times is the stack called? 
# function nesting requries a lot of memory in the stack
# I must reach the end of the tree so h = log2(n) if it is balanced
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
     
        def dfs(root):
            if not root :
                return None

            temp = root.left
            root.left = root.right
            root.right = temp
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return root
            


        