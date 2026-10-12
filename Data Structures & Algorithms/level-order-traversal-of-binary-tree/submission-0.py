# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        retval = [[]]
        queue = deque()
        queue.append((root, 0))

        while queue:
            curr, level = queue.popleft()
            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
            if len(retval) >= level + 1:
                retval[level].append(curr.val)
            else:
                retval.append([curr.val])

        return retval