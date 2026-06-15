# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        pre_slow = None
        slow = fast = head

        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        pre_slow.next = slow.next
    
        return head