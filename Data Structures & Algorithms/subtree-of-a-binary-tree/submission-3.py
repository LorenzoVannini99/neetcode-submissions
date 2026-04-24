class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Idea :
        # use an helper function called is Subtree
        
        if root and not subRoot or subRoot and not root:
            return False
                   
        def is_same_tree(p, q):

            if not p and q or not q and p :
                return False
            
            if not p and not q :
                return True

            if p.val != q.val :
                return False

            l = is_same_tree(p.left, q.left)    
            r = is_same_tree(p.right, q.right) 

            return (l and r)


        if is_same_tree(root, subRoot):
            return True
        else :

            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
        
            return (l or r)
  

