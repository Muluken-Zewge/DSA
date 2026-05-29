class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float("inf")

        for n in nums:
            curr_sum = 0
            while n > 0:
                curr_sum += n % 10
                n //= 10
            min_sum = min(min_sum,curr_sum)
        
        return min_sum