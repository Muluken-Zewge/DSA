class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # binary = bin(n)[2:]

        # for i in range(1,len(binary)):
        #     if binary[i] == binary[i-1]:
        #         return False
        
        # return True

        # --- bit manipulation version ---
        x = n ^ (n >> 1) # alternating bits give all 1's
        
        return x & (x + 1) == 0