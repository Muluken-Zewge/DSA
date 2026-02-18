# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        UNBALANCED = -1
        
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == UNBALANCED:
                return UNBALANCED

            right = height(node.right)
            if right == UNBALANCED:
                return UNBALANCED

            if abs(left - right) > 1:
                return UNBALANCED

            return max(left, right) + 1

        return height(root) != UNBALANCED
