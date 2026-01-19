class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        ans = float("inf")

        for i in range(n + 1):
            # Try to shrink from the left
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq[0])
                dq.popleft()

            # Maintain increasing prefix sums
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return -1 if ans == float("inf") else ans