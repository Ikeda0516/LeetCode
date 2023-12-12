class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        mid = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[mid])
        root.left = self.buildTree(preorder,inorder[:mid])
        root.right = self.buildTree(preorder,inorder[mid+1:])
        return root