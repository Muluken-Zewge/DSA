# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # step 1: do inorder traversal to get sorted value of the nodes
        arr = []
        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
    
        # step 2: build balanced BST recursively 
        def build_balanced_BST(arr,start,end):
            if start > end:
                return None
            
            # find the middle element of the current range
            mid = start + (end - start) // 2

            # recutsively construct the left and right sub trees
            left = build_balanced_BST(arr,start,mid-1)
            right = build_balanced_BST(arr,mid+1,end)

            # create new node with middle element and attach the subtress
            node = TreeNode(arr[mid],left,right)
            return node
        
        return build_balanced_BST(arr,0,len(arr)-1)
