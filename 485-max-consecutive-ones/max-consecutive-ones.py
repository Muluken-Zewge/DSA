class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = -1
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                start = -1
            else:
                if start == -1:
                    start = i
                
                max_ones = max(max_ones, i - start + 1)
        
        return max_ones