class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        heap = []
        ans = []

        for num in nums:
            counter[num] += 1
        
        for num in counter:
            heappush(heap,(counter[num],num))
            if len(heap) > k:
                heappop(heap)
        
        for _,num in heap:
            ans.append(num)
        
        return ans