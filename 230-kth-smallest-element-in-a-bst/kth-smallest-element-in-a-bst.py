# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None

        def inorder(node):
            nonlocal count, ans
            if not node or ans is not None:
                return
            
            inorder(node.left)
            count += 1
            if count == k:
                ans = node.val
                return
            
            inorder(node.right)
        
        inorder(root)
        return ans