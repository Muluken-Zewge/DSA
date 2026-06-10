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

    # bucket sort implementation(O(n) time and space complexity) 
    
    # freq = defaultdict(int)

    #     for n in nums:
    #         freq[n] += 1

    #     buckets = [[] for _ in range(len(nums) + 1)]
    #     print(buckets)

    #     for num, count in freq.items():
    #         buckets[count].append(num)
    #     print(buckets)

    #     ans = []

    #     for f in range(len(buckets) - 1, 0, -1):
    #         for num in buckets[f]:
    #             ans.append(num)
    #             if len(ans) == k:
    #                 return ans