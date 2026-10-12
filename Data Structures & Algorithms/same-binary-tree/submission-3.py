# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        seenP = [p.val if p else None]
        seenQ = [q.val if q else None]
        def recur(root, seen):
            if root:
                seen.append(root.left.val) if root.left else seen.append(None)
                seen.append(root.right.val) if root.right else seen.append(None)
                recur(root.left, seen)
                recur(root.right, seen)
            return seen

        recur(p, seenP)
        recur(q, seenQ)

        return seenP == seenQ