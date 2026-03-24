class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 # consecutive ones counter
        ans = 0
        for n in nums:
            if n == 1:
                count += 1
                ans = max(ans,count)
            else:
                count = 0
        
        return ans