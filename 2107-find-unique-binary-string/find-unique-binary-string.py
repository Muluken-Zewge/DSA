class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """since nums has n strings, iterating over n+1 possible strings
        guarantees a valid answer. convert the given strings to decimal and
        iterate from 0 to n. add enough zero's if the lenght of the binary
        representation of the number is less than n.
        """
        integers = set()
        for num in nums:
            integers.add(int(num, 2))

        n = len(nums)
        for num in range(n + 1):
            if num not in integers:
                ans = bin(num)[2:]
                return "0" * (n - len(ans)) + ans
            
        return ""