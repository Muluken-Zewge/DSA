class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_diff = max(nums) - min(nums)
        
        return max_diff * k