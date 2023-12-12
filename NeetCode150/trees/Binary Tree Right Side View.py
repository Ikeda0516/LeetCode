class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        maxLevel = -1

        def dfs(node, level):
            nonlocal ans, maxLevel
            if not node:
                return

            if maxLevel < level:
                maxLevel = level
                ans.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return ans