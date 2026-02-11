# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(root):
            if not root:
                return 
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)

        return ans


        # --- interative version ---

        # ans = []
        # stack = []

        # while root:
        #     ans.append(root.val)
        #     left = root.left
        #     right = root.right
        #     if right:
        #         stack.append(right)
        #     if not left and stack:
        #         root = stack.pop()
        #     else:
        #         root = left
        
        # return ans