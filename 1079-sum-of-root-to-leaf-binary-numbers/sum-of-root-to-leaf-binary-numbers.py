# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # use bit manipulation
        # left shift to create space for the new bit and ORed it with the new bit to add it to the number

        def dfs(node,curr):
            if not node:
                return 0

            # calulate curr value
            curr = (curr << 1) | node.val

            # if leaf node -> return completed number
            if not node.left and not node.right:
                return curr
            
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left + right
        
        return dfs(root,0)

        # --- iterative version ---
        # total = 0
        # stack = [(root,0)] # (node,curr_binary_val)

        # while stack:
        #     node, curr = stack.pop()

        #     # calculate the new curr value
        #     curr = (curr << 1) | node.val

        #     # if node is leaf, add to total
        #     if not node.left and not node.right:
        #         total += curr
        #     else:
        #         if node.left:
        #             stack.append((node.left,curr))
        #         if node.right:
        #             stack.append((node.right,curr))
            
        # return total