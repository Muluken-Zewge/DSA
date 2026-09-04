# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        before = head
        curr = head.next
        after = head.next.next

        min_dist = float("inf")
        first = last = latest =  None
        index = 0

        while after:
            index += 1
            if (before.val > curr.val and after.val > curr.val) or (curr.val > before.val and curr.val > after.val):
                if first is None:
                    first = index
                else:
                    min_dist = min(min_dist,index - latest)
                    last = index
                latest = index
            before = before.next
            curr = curr.next
            after = after.next

        if first is None or last is None:
            return [-1,-1]
        max_dist = last - first

        return [min_dist,max_dist]
