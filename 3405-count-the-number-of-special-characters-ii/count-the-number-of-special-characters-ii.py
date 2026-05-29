class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # last occurance of lowercase c should be before first occurance of uppercase c
        last_lower = {}
        first_upper = {}

        for i,c in enumerate(word):
            if c.islower():
                last_lower[c] = i
            else:
                lower = c.lower()
                if lower not in first_upper:
                    first_upper[lower] = i
        
        ans = 0
        for c in last_lower:
            if c in first_upper and last_lower[c] < first_upper[c]:
                ans += 1
        
        return ans