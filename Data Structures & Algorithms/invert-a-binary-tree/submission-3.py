# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Think about each layer, each node
# for each layer, swap left and right
# if it is none, well you have reached a leaf --> do nothing
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
            


        