# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def recur(root):
            nonlocal isBalanced
            if root and isBalanced:
                heightL = recur(root.left)
                heightR = recur(root.right)
                if abs(heightL - heightR) > 1:
                    isBalanced = False
                return max(heightL, heightR) + 1
            else:
                return 0
        recur(root)
        return isBalanced