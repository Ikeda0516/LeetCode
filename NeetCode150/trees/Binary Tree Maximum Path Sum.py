class Solution(object):
    def maxPathSum(self, root):
        ans = -10 ** 20
        
        def rec(node):
            nonlocal ans
            if not node:
                return 0
            l = rec(node.left)
            r = rec(node.right)
            ans = max(ans, node.val + l + r)
            return max(node.val + max(l, r), 0)
        
        rec(root)
        return ans