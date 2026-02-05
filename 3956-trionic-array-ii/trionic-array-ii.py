class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        NEG = float('-inf')

        dp0 = nums[0]
        dp1 = dp2 = dp3 = NEG
        ans = NEG

        for i in range(1, len(nums)):
            a, b = nums[i - 1], nums[i]

            ndp0 = b
            ndp1 = ndp2 = ndp3 = NEG

            if b > a:
                ndp1 = max(dp0, dp1) + b
                ndp3 = max(dp2, dp3) + b

            if b < a:
                ndp2 = max(dp1, dp2) + b

            dp0, dp1, dp2, dp3 = ndp0, ndp1, ndp2, ndp3
            ans = max(ans, dp3)

        return ans