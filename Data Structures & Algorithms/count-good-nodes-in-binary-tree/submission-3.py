class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Idea :
        # Think recursively, if i am at node root ( the first node )
        # the total good nodes is the sum of good nodes from left and from right
        # so you should return res = res_from_left + res_from_right
        # I only need as information the maximum seen so far
        # for example :
        # if a node at the left is greater than the node
        # the res from now on is 1 ( since i have found a good node )
        # technically a root node is a good node
        # if a node at the left is less or equal to the node
        # the res from now on is 0 


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

        
#       3
#      / \
#     1   4
#    /   / \
#   3   1   5
# Step by step:


#good node → res = 1
#left child is 1, maximum = 3 -> bad node -> res = 0
#left child is 3, maximum = 3 -> bad node -> res = 1
#pop from 3 res = 1
#pop from 1 res = 0 + 1 + 0 = 1
#we are at the root = 3
#right child is 4, maximum = 4 -> good node, res = 1
#left child is 1, bad node res = 0
#pop from 1, we go to the right
#5 is > 4, good node , res = 1
#pop from 5
# we are at 4 res = 1 + 0 + 1 = 2
# res = 1 + 1 + 2 = 4


