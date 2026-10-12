# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if root and not subRoot or not root and subRoot:
                return False
            if not root and not subRoot:
                return True
            if root.val == subRoot.val:
                isLeftSubtree = isSameTree(root.left, subRoot.left)
                isRightSubtree = isSameTree(root.right, subRoot.right)
                return isLeftSubtree and isRightSubtree
            else:
                return False
        
        def recur(root):
            if not root:
                return False
            if isSameTree(root, subRoot):
                return True
            else:
                return recur(root.left) or recur(root.right)
        return recur(root)