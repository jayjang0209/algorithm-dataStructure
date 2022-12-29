class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = self.find_length(head)

        if length <= 2:
            return head

        i = 0
        print(i)
        current = head
        # 10 -> -9 -> 6 -> -4 -> 1 -> 29 -> -1 -> None
        while i < length // 2:
            temp_next = current.next.next
            odd_node = ListNode(current.next.val)
            current = self.push_back(current, odd_node.val)
            current.next = temp_next
            current = current.next
            i += 1
            print(i)
        return head

    def find_length(self, head):
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        return length

    def push_front(self, head, new_element):
        new_node = ListNode(new_element)
        new_node.next = head
        return new_node

    def push_back(self, head, new_value):
        new_node = ListNode(new_value)
        if head is None:
            return new_node
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
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
    a1 = ListNode(1)
    a2 = ListNode(1)
    # a3 = ListNode(6)
    # a4 = ListNode(-4)
    # a5 = ListNode(1)
    # a6 = ListNode(29)
    # a7 = ListNode(-1)
    a1.next = a2
    # a2.next = a3
    # a3.next = a4
    # a4.next = a5
    # a5.next = a6
    # a6.next = a7
    print(solution.print_list(a1))
    # sorted_list = solution.sortArray(unsorted_list)
    ans = solution.oddEvenList(a1)
    print(solution.print_list(ans))


if __name__ == "__main__":
    main()
