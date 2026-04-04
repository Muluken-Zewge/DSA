class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)
        for _ in range(k-1):
            heappop(nums)
        
        return -nums[0]