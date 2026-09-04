# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        def inorder(node):
            nonlocal nums
            if node is None:
                return 
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)

        return nums[k-1]