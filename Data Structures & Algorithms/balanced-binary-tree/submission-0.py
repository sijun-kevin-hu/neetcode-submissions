# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        return left and right and abs(left_height - right_height) <= 1

    def getHeight(self, node):
        if not node:
            return 0
        
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        return 1 + max(left, right)