class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Idea :
        # Think recursively, if i am at node root ( the first node )
        # the total good nodes is the sum of good nodes from left and from right
        # i only need to return the maximum
        # if a node.val at the left is > than the maximum i have one more good node
        # so the number of good node from left on is 1
        # if it's not the number of good nodes from left node is 0

        def dfs( root, maximum) :

            if not root :
                return 0
            
            if root.val >= maximum :
                res = 1
            else :
                res = 0    

            maximum = max (root.val, maximum)

            res = res + dfs(root.left, maximum) + dfs(root.right, maximum)

            return res

        return dfs ( root, root.val)

        



