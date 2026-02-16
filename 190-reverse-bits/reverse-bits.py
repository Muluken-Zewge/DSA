class Solution:
    def reverseBits(self, n: int) -> int:
        bi = ''
        while n > 0:
            bi += str(n % 2)
            n //= 2

        while len(bi) < 32:
            bi += '0'

        return int(bi,2)