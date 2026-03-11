class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit_count = len(bin(n)[2:])
        for i in range(bit_count):
            n ^= (1 << i)
        return n