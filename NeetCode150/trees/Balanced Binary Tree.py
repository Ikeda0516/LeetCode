class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        
        l = self.depth(root.left)
        r = self.depth(root.right)
        return abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1