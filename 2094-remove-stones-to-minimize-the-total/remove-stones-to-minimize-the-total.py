class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapify(piles)
        
        for _ in range(k):
            max_val = -heappop(piles)
            new_val = max_val - (max_val // 2)
            heappush(piles,-new_val)
        
        return -sum(piles)