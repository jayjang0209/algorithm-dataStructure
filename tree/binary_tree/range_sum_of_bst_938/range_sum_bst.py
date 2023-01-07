"""
938. Range Sum of BST

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        return self.preorder_traverse(root, low, high)

    def preorder_traverse(self, root, l, h):
        if not root:
            return 0

        if l <= root.val <= h:
            add = root.val
        else:
            add = 0

        return add + self.preorder_traverse(root.left, l, h) + self.preorder_traverse(root.right, l, h)