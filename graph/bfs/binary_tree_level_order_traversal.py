"""
102. Binary Tree Level Order Traversal

Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  # Time complexity: O(N)
  # Space complexity: O(N)

  def traverse(self, root):
    result = []
    if root is None:
      return result

    queue = deque()
    queue.append(root)

    while queue:
      nodes_in_cur_level = []

      for _ in range(len(queue)):
        v = queue.popleft()
        nodes_in_cur_level.append(v.val)

        if v.left:
          queue.append(v.left)
        if v.right:
          queue.append(v.right)
      
      result.append(nodes_in_cur_level)
    return result
