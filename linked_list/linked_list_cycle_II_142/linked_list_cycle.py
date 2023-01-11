# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Hash Table
    # Time: O(n) visit each of the n elements. adding to set(hash table) constant
    # Space: O(n) hash table
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return None

        seen = set()

        current = head
        while current:
            if current in seen:
                return current
            seen.add(current)
            current = current.next
        return None
