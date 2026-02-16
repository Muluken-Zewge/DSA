class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = binary[::-1]
        while len(binary) < 32:
            binary += '0'
        return int(binary,2)