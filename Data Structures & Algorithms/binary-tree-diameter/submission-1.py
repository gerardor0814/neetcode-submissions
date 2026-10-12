# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        globalMax = 0

        def height(root):
            if root:
                return max(height(root.left), height(root.right)) + 1
            else:
                return 0
        def recur(root):
            nonlocal globalMax
            if root:
                heightR = height(root.right)
                heightL = height(root.left)
                globalMax = max(globalMax, heightR + heightL)
                recur(root.left)
                recur(root.right)
        recur(root)
        return globalMax
