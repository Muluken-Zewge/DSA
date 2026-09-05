# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        min_dist = float("inf")
        first_cp = prev_cp = None
        i = 1

        while curr.next:
            if (curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val):
                if first_cp is None:
                    first_cp = i
                else:
                    min_dist = min(min_dist, i - prev_cp)
                
                prev_cp = i

            i += 1
            prev = curr
            curr = curr.next
        
        if first_cp is None or first_cp == prev_cp:
            return [-1,-1]
        max_dist = prev_cp - first_cp

        return [min_dist,max_dist]