# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node):
            if not node:
                return None
            if node.val == val:
                return node
            if val < node.val:
                return search(node.left)
            if val > node.val:
                return search(node.right)   
                     
        return search(root)

        # --- iterative verson ---
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node is None:
        #         return None
        #     if val == node.val:
        #         return node
        #     if val < node.val:
        #         stack.append(node.left)
        #     if val > node.val:
        #         stack.append(node.right)