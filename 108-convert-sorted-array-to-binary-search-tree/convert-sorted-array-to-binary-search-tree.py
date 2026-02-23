# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # use devide and conquer algorithm
        def build_balaned_BST(arr,start,end):
            if start > end:
                return None
            # find mid 
            mid = start + (end - start) // 2
            
            # construct left and right sub tree
            left = build_balaned_BST(arr,start,mid-1)
            right = build_balaned_BST(arr,mid+1,end)

            # create new node and attach left and right sub tree
            node = TreeNode(arr[mid],left,right)
            return node

        return build_balaned_BST(nums,0,len(nums)-1)