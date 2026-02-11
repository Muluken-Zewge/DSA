# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []

        # def inorder(root):
        #     if not root:
        #         return
            
        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)
        
        # inorder(root)

        # return ans

        ans = []
        stack = []

        while root or stack:
            # go to left most node
            while root:
                stack.append(root)
                root = root.left

            # process the node
            curr = stack.pop()
            ans.append(curr.val)

            # go to right
            root = curr.right
        
        return ans