# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dum = ListNode()
        ans_head = dum
        while list1 and list2:
            if list1.val <= list2.val:
                dum.next = ListNode(list1.val)
                dum = dum.next
                list1 = list1.next
            else:
                dum.next = ListNode(list2.val)
                dum = dum.next
                list2 = list2.next

        if list1:
            dum.next = list1
        if list2:
            dum.next = list2
        return ans_head.next


a1 = ListNode(-10)
a2 = ListNode(-9)
a3 = ListNode(-6)
a4 = ListNode(-4)
a5 = ListNode(1)
a6 = ListNode(9)
a7 = ListNode(9)
b1 = ListNode(-5)
b2 = ListNode(-3)
b3 = ListNode(0)
b4 = ListNode(7)
b5 = ListNode(8)
b6 = ListNode(8)


a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5
b5.next = b6

s = Solution()
ans = s.mergeTwoLists(a1, b1)
print(ans)

