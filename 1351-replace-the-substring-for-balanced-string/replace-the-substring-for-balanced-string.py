'''we use sliding window but slightly in a different way. we count the number of chars outside the window and check that count is <= the target count(n//4) for all chars. if so, valid window, shrink. 
'''
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        t = n // 4 # target count
        counter = Counter(s) # count outside of window

        if all(counter[c] == t for c in "QREW"):
            return 0

        l = 0 # left pointer
        ans = n

        for r in range(n):
            counter[s[r]] -= 1
            while all(counter[c] <= t for c in "QREW"):
                ans = min(ans,r - l + 1)
                counter[s[l]] += 1
                l += 1

        return ans              