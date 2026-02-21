class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # count set bits
        def count_set_bit(n):
            set_bits = 0
            while n > 0:
                set_bits += 1
                n = n & (n-1)
            
            return set_bits

        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0
        for i in range(left, right+1):
            if count_set_bit(i) in primes:
                count += 1
        
        return count