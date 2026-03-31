# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def findPath(root,node):
            path = []
            curr = root
            
            while curr:
                path.append(curr.val)
                if node.val < curr.val:
                    curr = curr.left
                elif node.val > curr.val:
                    curr = curr.right
                else:
                    break
            
            return path
        
        path_p = findPath(root,p)
        path_q = findPath(root,q)
        
        i = (min(len(path_p), len(path_q)) - 1)
        while i >= 0:
            if path_p[i] == path_q[i]:
                return TreeNode(path_q[i])
            i -= 1
        