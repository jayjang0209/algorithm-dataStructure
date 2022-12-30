class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    if root is not None:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def inorder_traversal(root: TreeNode):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)
