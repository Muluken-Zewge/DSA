class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        longest = 0

        for i in range(n):
            counter = defaultdict(int)
            for j in range(i,n):
                counter[s[j]] += 1
                
                # check if all chars appears equal number of times
                if len(set(counter.values())) == 1:
                    longest = max(longest, j - i + 1)
        
        return longest
