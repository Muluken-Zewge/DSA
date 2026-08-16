# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        curr = []

        def dfs(node,curr):
            if not node:
                return
            curr.append(node.val)
            
            if node.left is None and node.right is None:
                if sum(curr) == targetSum:
                    ans.append(curr)
            dfs(node.left,curr[:])
            dfs(node.right,curr[:])
        
        dfs(root,curr)
        return ans