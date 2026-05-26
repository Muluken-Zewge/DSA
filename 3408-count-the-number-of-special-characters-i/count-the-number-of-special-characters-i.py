class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        special = 0
        seen_upper = set()

        for c in word:
            if c.islower():
                lower.add(c)
        
        for c in word:
            if c.isupper() and c.lower() in lower and c not in seen_upper:
                special += 1
                seen_upper.add(c)
        
        return special