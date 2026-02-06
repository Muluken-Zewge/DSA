class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = n
        i = 0

        for j in range(n):
            while nums[j] > nums[i]*k:
                i += 1
            
            ans = min(ans, n - (j - i + 1))
        
        return ans