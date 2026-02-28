class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """concatinating a new number means left shifting the current
        number by the number of bits of the new number(creating a space for
        the new bits) and ORing with the new number. the way we counted bit
        number is from the fact that a bit number increases by one when the
        number is a power of two
        """
        MOD = 10 ** 9 + 7
        res = 0
        length = 0 # current bit length

        for i in range(1,n+1):
            # increase bit count if i is power of two
            if i & (i-1) == 0:
                length += 1
            
            res = ((res << length) | i) % MOD
        
        return res