class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]

        def traverse(node):
            if not node:
                return 
            l.append(node.val)
            traverse(node.left)
            traverse(node.right)
       
        traverse(root)
        l = list(set(l))
        return l[k - 1]