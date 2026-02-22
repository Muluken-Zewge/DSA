class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        start = -1
        longest = 0

        for i in range(len(binary)):
            if binary[i] == '1':
                if start == -1:
                    start = i
                else:
                    longest = max(longest, i - start)
                    start = i
        

        return longest