class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # find the length of the linked list
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        # calculate the size of each part
        # Hint: If there are N nodes in the list, and k parts,
        # then every part has N/k elements, except the first N%k parts have an extra one.
        part_size, longer_parts = divmod(length, k)

        # Init the result list
        result = [None] * k

        # Split the linked list into k parts
        curr = head
        for i in range(k):
            result[i] = curr

            for j in range(part_size + (i < longer_parts) - 1):
                if curr:
                    curr = curr.next

            if curr:
                temp = curr.next
                curr.next = None
                curr = temp
        return result


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
    a6 = ListNode(6)
    a7 = ListNode(7)
    a8 = ListNode(8)
    a9 = ListNode(9)
    a10 = ListNode(10)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    a6.next = a7
    a7.next = a8
    a8.next = a9
    a9.next = a10
    print(solution.print_list(a1))
    ans = solution.splitListToParts(a1, 3)
    print(ans)
    for link in ans:
        print(solution.print_list(link))


if __name__ == "__main__":
    main()
