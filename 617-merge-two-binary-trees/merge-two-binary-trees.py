# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(node1,node2):
            if not node1 and not node2:
                return None
            
            val = (node1.val if node1 else 0) + (node2.val if node2 else 0)
            new_node = TreeNode(val)

            new_node.left = merge(node1.left if node1 else None,node2.left if node2 else None)
            new_node.right = merge(node1.right if node1 else None,node2.right if node2 else None)

            return new_node
        
        return merge(root1,root2)
