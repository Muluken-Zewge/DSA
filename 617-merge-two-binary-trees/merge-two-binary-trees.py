# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merge(node1,node2):
            # base case
            if node1 is None and node2 is None:
                return None
            
            if node1 is None:
                new_node = TreeNode(node2.val)
                left = merge(None,node2.left)
                right = merge(None,node2.right)
                new_node.left = left
                new_node.right = right
                return new_node
            elif node2 is None:
                new_node = TreeNode(node1.val)
                left = merge(node1.left,None)
                right = merge(node1.right,None)
                new_node.left = left
                new_node.right = right
                return new_node
            else: # both are not none
                new_node = TreeNode(node1.val + node2.val)
                left = merge(node1.left,node2.left)
                right = merge(node1.right,node2.right)
                new_node.left = left
                new_node.right = right
                return new_node
        
        return merge(root1,root2)