class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        special = 0
        seen = set()

        for c in word:
            if c.islower():
                lower.add(c)
        
        for c in word:
            if c.isupper() and c.lower() in lower and c not in seen:
                special += 1
                seen.add(c)
        
        return special