"""
LeetCode 100.Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
https://leetcode.com/problems/same-tree/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        first = []
        second = []
        self.preorder_traversal(first, p)
        self.preorder_traversal(second, q)
        print(first)
        print(second)
        return first == second

    def preorder_traversal(self, result, root):  # inorder didn't work
        if root:
            result.append(root.val)
            self.preorder_traversal(result, root.left)
            self.preorder_traversal(result, root.right)
        else:
            result.append(None)
