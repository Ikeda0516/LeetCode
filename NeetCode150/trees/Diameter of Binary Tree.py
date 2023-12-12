class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            l = dfs(node.right)
            r = dfs(node.left)
            ans = max(ans, l + r)

            return max(l, r) + 1
        
        dfs(root)
        return ans