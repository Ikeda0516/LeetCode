class Codec:
    def serialize(self, root):
        if not root:
            return ""
        mid = str(root.val)
        l = str(self.serialize(root.left))
        r = str(self.serialize(root.right))
        return mid + ',' + l + ',' + r

    def deserialize(self, data: str):
        if not data:
            return None
        return self.deserializeList(data.split(','))

    def deserializeList(self, nums: List[str]):
        val = nums.pop(0)
        if not val:
            return None
        
        root = TreeNode(val)
        root.left = self.deserializeList(nums)
        root.right = self.deserializeList(nums)

        return root