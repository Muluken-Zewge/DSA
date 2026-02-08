class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # (total - global_min) gives the circualr answer and we caomare it with the normal kadane sum
        global_max, global_min = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for n in nums:
            curr_max = max(n, n + curr_max)
            curr_min = min(n, n + curr_min)
            total += n
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)
        
        if global_max < 0: # all numbers are negative
            return global_max
        
        return max(global_max, total - global_min)