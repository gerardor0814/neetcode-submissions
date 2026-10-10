"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':   
        if not head:
            return
        newNodes = {}
        curr = head
        while curr:
            newNodes[curr] = (Node(curr.val, None, None))
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                newNodes[curr].next = newNodes[curr.next]
            if curr.random:
                newNodes[curr].random = newNodes[curr.random]
            curr = curr.next

        return newNodes[head]