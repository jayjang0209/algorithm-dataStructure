"""
Easy
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        if fast is None:
            second_half = slow
        else:
            second_half = slow.next

        return second_half

    def print_list(self, head):
        node = head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


def main():
    solution = Solution()
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    # a6 = ListNode(6)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    # a5.next = a6
    ans = solution.middleNode(a1)
    print(solution.print_list(ans))


if __name__ == "__main__":
    main()
