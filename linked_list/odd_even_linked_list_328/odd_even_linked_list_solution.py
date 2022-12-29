"""
Solution by LeetCode
https://leetcode.com/problems/odd-even-linked-list/solutions/127831/odd-even-linked-list/
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

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
    a1 = ListNode(0)
    a2 = ListNode(10)
    a3 = ListNode(6)
    a4 = ListNode(-4)
    a5 = ListNode(1)
    a6 = ListNode(29)
    a7 = ListNode(-1)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    a6.next = a7
    print('original')
    print(solution.print_list(a1))
    # sorted_list = solution.sortArray(unsorted_list)
    print('answer')
    ans = solution.oddEvenList(a1)
    print(solution.print_list(ans))


if __name__ == "__main__":
    main()
