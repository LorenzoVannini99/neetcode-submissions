# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Let's think recursively of course
# at each node the depth is
# what the max gives me + what the right gives + 1 beacuse this node exists
# if a node is None return 0

# TC : O(n)
# SC : O(h) where h = log(n) is balanced
# at most SC is O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return max(l, r) + 1    



        