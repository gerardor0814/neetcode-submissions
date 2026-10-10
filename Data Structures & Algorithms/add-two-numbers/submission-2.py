# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        list1 = l1
        list2 = l2
        res = 0

        while list1 and list2:
            s = list1.val + list2.val + res
            if s >= 10:
                res = 1
                s -= 10
            else:
                res = 0
            curr.next = ListNode(s, None)
            curr = curr.next
            list1 = list1.next
            list2 = list2.next

        longer = list1 or list2

        while longer:
            s = longer.val + res
            if s >= 10:
                res = 1
                s -= 10
            else:
                res = 0
            curr.next = ListNode(s, None)
            curr = curr.next
            longer = longer.next
        
        if res:
            curr.next = ListNode(1)

        return dummy.next