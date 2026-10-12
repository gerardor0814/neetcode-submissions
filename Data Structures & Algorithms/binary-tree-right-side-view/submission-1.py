# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        retval = []
        queue = deque()
        queue.append(root)

        while queue:
            lenqueue = len(queue)
            
            curr = None
            for i in range(lenqueue):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            retval.append(curr.val)
        return retval