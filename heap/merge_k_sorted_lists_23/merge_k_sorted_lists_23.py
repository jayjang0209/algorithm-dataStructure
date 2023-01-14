# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list):
        if len(lists) == 0:
            return None

        min_heap = []
        for list in lists:
            while list:
                heapq.heappush(min_heap, list.val)
                list = list.next

        dummy_head = ListNode(-1)
        head = dummy_head
        for i in range(len(min_heap)):
            dummy_head.next = ListNode(heapq.heappop(min_heap))
            dummy_head = dummy_head.next
        return head.next

