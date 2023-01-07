"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        return self.is_symmetric(root, root)

    def is_symmetric(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.is_symmetric(p.right, q.left) and self.is_symmetric(p.left, q.right)

