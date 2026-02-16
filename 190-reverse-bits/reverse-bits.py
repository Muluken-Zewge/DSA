class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            res <<= 1 # make a space for the last bit of n
            res = res | (n & 1) # extract last bit of n(n & 1), add to res
            n >>= 1 # move to the next bit
        
        return res
