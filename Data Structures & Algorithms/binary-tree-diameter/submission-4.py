# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        globalMax = 0

        def diameter(root):
            nonlocal globalMax
            if root:
                heightR = diameter(root.right)
                heightL = diameter(root.left)
                globalMax = max(globalMax, heightR + heightL)
                return max(heightR, heightL) + 1
            else:
                return 0

        diameter(root)
        return globalMax
