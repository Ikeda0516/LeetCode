class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        INF = 10 ** 20
        
        def rec(node, Min, Max):
            if not node:
                return True

            if Min < node.val < Max:
                return rec(node.left, Min, node.val) and rec(node.right, node.val, Max)
            else:
                return False
        
        return rec(root, -INF, INF)