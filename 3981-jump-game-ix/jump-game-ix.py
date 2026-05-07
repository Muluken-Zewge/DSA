class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
      
        # Build prefix maximum array
        pre_max = [nums[0]] * n
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])
      
        suf_min = float('inf')
      
        # Process from right to left
        for i in range(n - 1, -1, -1):
            if i + 1 < n:
                # Can potentially jump forward and utilize future possibilities
                ans[i] = ans[i + 1] if pre_max[i] > suf_min else pre_max[i]
            else:
                # Last element: maximum reachable is pre_max[i]
                ans[i] = pre_max[i]
          
            # Update suffix minimum after processing current position
            suf_min = min(suf_min, nums[i])
      
        return ans