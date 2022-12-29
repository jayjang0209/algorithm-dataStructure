import math

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
        ans = []
        linked_list_len = self.find_length(head)
        num_element_per_parts = int(math.floor(linked_list_len / k))
        num_parts_with_extra = linked_list_len % k

        for i in range(k):
            part_head = ListNode(-1)
            part_head_pointer = part_head
            num_loop = num_element_per_parts + 1 if i < num_parts_with_extra \
                else num_element_per_parts
            for j in range(num_loop):
                part_head.next = ListNode(head.val)
                part_head = part_head.next
                head = head.next

            if part_head_pointer.val == -1 and part_head_pointer.next:
                part_head_pointer = part_head_pointer.next
            else:
                part_head_pointer = None
            ans.append(part_head_pointer)
        return ans



    def find_length(self, head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length


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
