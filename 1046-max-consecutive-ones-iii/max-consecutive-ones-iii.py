class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flip = 0 # number of flipped 0's
        l = 0 # left pointer
        max_ones = 0 

        for r in range(len(nums)):
            if nums[r] == 0:
                flip += 1
            
            while flip > k:
                if nums[l] == 0:
                    flip -= 1
                l += 1
            
            max_ones = max(max_ones, r - l + 1)
        
        return max_ones