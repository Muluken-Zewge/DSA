class Solution:
    def hammingWeight(self, n: int) -> int:
        # Brian Kernighan’s algorithm
        set_bits = 0
        while n > 0:
            set_bits += 1
            n = n & (n-1)
        
        return set_bits
        