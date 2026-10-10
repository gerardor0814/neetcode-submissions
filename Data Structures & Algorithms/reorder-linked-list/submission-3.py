# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        #slow head of new list
        prev = None
        while slow.next:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
        slow.next = prev

        curr = head
        head = head.next
        isHead = True
        while head and slow and head != slow:
            if isHead:
                curr.next = slow
                slow = slow.next
                isHead = not isHead
            else:
                curr.next = head
                head = head.next
                isHead = not isHead
            curr = curr.next
