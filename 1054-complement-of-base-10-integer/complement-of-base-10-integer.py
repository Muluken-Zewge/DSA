class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit_length = len(bin(n)[2:])
        mask = (1 << bit_length) - 1

        return n ^ mask