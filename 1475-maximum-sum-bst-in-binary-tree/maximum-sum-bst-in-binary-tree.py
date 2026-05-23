class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def dfs(node):
            nonlocal max_sum

            # is_bst, min_val, max_val, subtree_sum
            if not node:
                return True, float("inf"), float("-inf"), 0

            left_is_bst, left_min, left_max, left_sum = dfs(node.left)
            right_is_bst, right_min, right_max, right_sum = dfs(node.right)

            # Check if current subtree is BST
            if (left_is_bst and right_is_bst and left_max < node.val < right_min):
                curr_sum = left_sum + right_sum + node.val
                max_sum = max(max_sum, curr_sum)

                return True, min(left_min, node.val), max(right_max, node.val), curr_sum
            
            # Not a BST
            return False, 0, 0, 0

        dfs(root)

        return max_sum