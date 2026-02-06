class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = 1 # tracks the min showns so far
        max_prod = 1 # track the max shown so far
        res = float("-inf")

        for num in nums:
            min_prod0 = min_prod
            max_prod0 = max_prod

            min_prod = min(num, min_prod0*num, max_prod0*num)
            max_prod = max(num, min_prod0*num, max_prod0*num)
            res = max(res, min_prod, max_prod)
        
        return res