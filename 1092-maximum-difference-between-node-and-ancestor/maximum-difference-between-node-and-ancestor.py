# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, curr_min, curr_max):
            nonlocal ans
            if not node:
                return
            max_diff = max(abs(node.val - curr_min), abs(node.val - curr_max))
            ans = max(ans, max_diff)
            
            dfs(node.left,min(node.val,curr_min),max(node.val,curr_max))
            dfs(node.right,min(node.val,curr_min),max(node.val,curr_max))
        
        dfs(root, root.val, root.val)

        return ans