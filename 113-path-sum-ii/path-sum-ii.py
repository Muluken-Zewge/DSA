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
                return 0
            curr.append(node.val)
            left = dfs(node.left,curr[:])
            right = dfs(node.right,curr[:])
            if left == 0 and right == 0:
                print(curr)
                if sum(curr) == targetSum:
                    ans.append(curr)
            return 1
        
        dfs(root,curr)
        return ans