"""
938. Range Sum of BST

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

    """
    This solution works by recursively traversing the tree and adding the value of the current node to the sum 
    if it is within the specified range. If the value of the current node is less than low, 
    then we know that all the nodes in the left subtree will also be less than low, so we can skip the left subtree 
    and only search the right subtree. If the value of the current node is greater than high, 
    then we know that all the nodes in the right subtree will also be greater than high, 
    so we can skip the right subtree and only search the left subtree. 
    If the value of the current node is within the range, then we add it to the sum and search both subtrees. 
    This solution has a time complexity of O(n), where n is the number of nodes in the tree.
    By ChatGPT
    """