class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return self.isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSametree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return s == t
        return s.val == t.val and self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)