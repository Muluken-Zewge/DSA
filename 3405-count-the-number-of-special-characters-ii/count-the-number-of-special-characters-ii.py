class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_cnt = defaultdict(int)
        seen_upper = set()
        special = 0
        for c in word:
            if c.islower():
                lower_cnt[c] += 1

        for c in word:
            if c.islower() and c not in seen_upper:
                lower_cnt[c] -= 1
            else:
                l = c.lower()
                if l in lower_cnt and lower_cnt[l] == 0 and c not in seen_upper:
                    special += 1
                seen_upper.add(c)
        
        return special