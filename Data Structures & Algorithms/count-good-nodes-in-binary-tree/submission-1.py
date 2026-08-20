class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node,maximum = -101) : 
            
            if not node :
                return 0

            if node.val >= maximum :
                maximum = node.val
                return 1 + dfs(node.left,maximum) + dfs(node.right,maximum)  
            else:
                return dfs(node.left,maximum) + dfs(node.right,maximum)

        return dfs(root)    
            

