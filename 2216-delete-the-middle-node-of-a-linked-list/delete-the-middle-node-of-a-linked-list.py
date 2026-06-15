# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find the length of the linked list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length == 1:
            return None
        
        mid = length // 2
        count = -1
        curr = head
        while curr:
            count += 1
            if count + 1 == mid:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head
