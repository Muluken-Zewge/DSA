class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = 1 # tracks the min showns so far
        max_prod = 1 # track the max shown so far
        global_max = float("-inf")

        for num in nums:
            prev_min = min_prod
            prev_max = max_prod

            min_prod = min(num, prev_min*num, prev_max*num)
            max_prod = max(num, prev_min*num, prev_max*num)
            global_max = max(global_max, max_prod)
        
        return global_max