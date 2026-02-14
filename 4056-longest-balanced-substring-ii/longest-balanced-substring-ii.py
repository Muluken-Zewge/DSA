class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        # Case 1: single char
        curr = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 1
        ans = max(ans, curr)

        # Case 2: two chars
        def solve_two(c1, c2):
            nonlocal ans
            diff_map = {0: -1}
            diff = 0
            for i in range(n):
                if s[i] == c1:
                    diff += 1
                elif s[i] == c2:
                    diff -= 1
                else:
                    # reset if third char appears
                    diff = 0
                    diff_map = {0: i}
                    continue

                if diff in diff_map:
                    ans = max(ans, i - diff_map[diff])
                else:
                    diff_map[diff] = i

        solve_two('a', 'b')
        solve_two('a', 'c')
        solve_two('b', 'c')

        # Case 3: three chars
        ca = cb = cc = 0
        mp = {(0, 0): -1}

        for i in range(n):
            if s[i] == 'a':
                ca += 1
            elif s[i] == 'b':
                cb += 1
            else:
                cc += 1

            key = (cb - ca, cc - ca)

            if key in mp:
                ans = max(ans, i - mp[key])
            else:
                mp[key] = i

        return ans
