# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        small = float("-inf")
        def dfs(root, i, k):
            nonlocal small
            if root:
                i = dfs(root.left, i, k)
                i += 1
                if i == k:
                    small = root.val
                i = dfs(root.right, i, k)
            return i
        dfs(root, 0, k)
        return small
