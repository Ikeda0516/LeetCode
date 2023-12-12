class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0

        def dfs(node, Max):
            nonlocal ans
            if not node:
                return 

            if Max <= node.val:
                Max = node.val
                ans += 1
            dfs(node.left, Max)
            dfs(node.right, Max)
        
        dfs(root, root.val)
        return ans