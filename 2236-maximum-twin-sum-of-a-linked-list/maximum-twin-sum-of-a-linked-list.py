# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # step 1. use two pointer approach to cut the list into half
        slow = fast = head
        pre_slow = None
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        pre_slow.next = None

        # step 2. reverse the second part of the list
        prev = None
        curr = slow
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        
        # step 3. use two pointer to find the max sum
        l = head
        r = prev # head of the reversed list
        max_sum = 0
        while l and r:
            max_sum = max(max_sum,l.val + r.val)
            l = l.next
            r = r.next
        
        return max_sum