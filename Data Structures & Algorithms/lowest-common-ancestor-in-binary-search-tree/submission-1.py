# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # Idea :
        # First p should always be to the left of q
        # if p == q --> return q
        # if p > q, tmp = q , q = p , p = tmp
        # start at the root, 
        # if root is < p , i need to go to the right ( res > root)
        # since p <= LCA <= q
        # if root is > q, i need to go to the left ( res < root )
        # if  p <= root <= q --> ( res = root )
        # res is a global variable, every dfs pass needs to know res

        if not p and not q :
            return 

        if not p and q or not q and p :
            return 
        
        if p.val == q.val :
            return p

        if p.val > q.val :
            tmp = q
            q = p
            p = tmp 
        
        self.res = root

        def dfs ( root ) :

            if not root :
                return

            if root.val < p.val:
                dfs(root.right) 

            if root.val > q.val:
                dfs(root.left)
            
            if p.val <= root.val <= q. val:
                    self.res = root
        
        dfs ( root )

        return self.res


      













