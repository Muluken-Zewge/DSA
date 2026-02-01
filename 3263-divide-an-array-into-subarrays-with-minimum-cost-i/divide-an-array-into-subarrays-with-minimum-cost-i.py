class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)

        # suffixMin[i] = min(nums[i..n-1])
        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        ans = float("inf")

        # i is the start of the second subarray
        for i in range(1, n - 1):
            cost = nums[0] + nums[i] + suffixMin[i + 1]
            ans = min(ans, cost)

        return ans