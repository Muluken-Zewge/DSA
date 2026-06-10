class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        min_heap = []

        for n in nums:
            counter[n] += 1
        
        for n in counter:
            heappush(min_heap,(counter[n],n))
            if len(min_heap) > k:
                heappop(min_heap)
        
        ans = [t[1] for t in min_heap]

        return ans