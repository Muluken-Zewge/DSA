# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []

        # def postorder(root):
        #     if not root:
        #         return 
            
        #     postorder(root.left)
        #     postorder(root.right)
        #     ans.append(root.val)
        
        # postorder(root)

        # return ans
        
        ans = []
        stack = []
        prev = None # last processed node

        while root or stack:
            # go as left as possible
            while root:
                stack.append(root)
                root = root.left
            
            node = stack[-1] # peek

            # right child exist and hasn't been processed
            if node.right and node.right != prev:
                root = node.right
            else:
                # right is None or already processed
                stack.pop()
                ans.append(node.val)
                prev = node # mark as processed
            
        return ans
