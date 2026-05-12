# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # do BFS and reverse order of elements when the level is odd
        queue = deque([root])
        level = 0
        ans = []
        if not root:
            return []

        while queue:
            size = len(queue)
            level_vals = []

            for _ in range(size):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                level_vals.reverse()
            
            ans.append(level_vals)
            level += 1

        return ans