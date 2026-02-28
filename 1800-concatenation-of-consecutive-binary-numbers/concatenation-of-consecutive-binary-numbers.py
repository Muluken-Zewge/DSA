class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        binary = ''
        i = 1

        while i <= n:
            binary += bin(i)[2:]
            i += 1

        return int(binary,2) % MOD