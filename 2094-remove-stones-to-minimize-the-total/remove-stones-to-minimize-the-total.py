class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for val in piles:
            heappush(max_heap,-val)
        
        while k > 0:
            max_val = -heappop(max_heap)
            new_val = max_val - (max_val // 2)
            heappush(max_heap,-new_val)
            k -= 1
        
        return -sum(max_heap)