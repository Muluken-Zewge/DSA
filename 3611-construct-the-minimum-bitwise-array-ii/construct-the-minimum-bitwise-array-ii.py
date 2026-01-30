class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            # impossible if n is even
            if n % 2 == 0:
                ans.append(-1)
                continue

            # count trailing 1s
            k = 0
            temp = n
            while temp & 1:
                k += 1
                temp >>= 1

            # remove the highest bit of the trailing-1s block
            x = n - (1 << (k - 1))
            ans.append(x)

        return ans
