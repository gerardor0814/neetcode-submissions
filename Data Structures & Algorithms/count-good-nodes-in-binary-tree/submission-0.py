# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodnodes = 0
        def dfs(root, maxval):
            nonlocal goodnodes
            if root:
                if root.val >= maxval:
                    goodnodes += 1
                    newmax = root.val
                else:
                    newmax = maxval
                dfs(root.left, newmax)
                dfs(root.right, newmax)
            else:
                return
        dfs(root, root.val)
        return goodnodes
