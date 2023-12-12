class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = defaultdict(list)

        def dfs(node, level):
            nonlocal levels
            if not node:
                return

            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return levels.values()