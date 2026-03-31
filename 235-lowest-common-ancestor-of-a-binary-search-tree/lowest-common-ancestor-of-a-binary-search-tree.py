# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # this was my original approach
        '''
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
    '''
        # this is the best approach
        '''if both p and q are less than the curr, the LCA is to the left.
        if both of them are greater than curr, the LCA is to the right.
        else: we have two cases: 
        1. p is in the right and q is in the left(or the reverse), then the
        curr is the BST. it doesn't matter how far p or q are in their
        subtree.
        2. p and q are in the same path, the LCA is the one on top(either p
        or q) which is equal to curr.
        '''
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
