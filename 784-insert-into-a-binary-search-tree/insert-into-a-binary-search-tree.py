# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # def insert(node,val):
        #     if node is None:
        #         return TreeNode(val)
        #     if val < node.val:
        #         node.left = insert(node.left,val)
        #         return node
        #     if val > node.val:
        #         node.right = insert(node.right,val)
        #         return node
        
        # return insert(root,val)

        if root is None:
            return TreeNode(val)

        stack = [root]
        while stack:
            node = stack.pop()
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    stack.append(node.left)
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    stack.append(node.right)
        
        return root