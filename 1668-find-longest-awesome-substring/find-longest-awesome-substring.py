class Solution:
    def longestAwesome(self, s: str) -> int:
        '''a string is palindrome if it has at most one odd count char while the rest
        has eve count. we use prefix difference approach with bitmasking to track the
        state of the string
        '''
        prefix_state = {0:-1}
        mask = 0
        ans = 0

        for i in range(len(s)):
            digit = int(s[i])

            # flip the bit for this digit
            mask ^= (1 << digit)

            # Case 1: all digits even (same mask seen before)
            if mask in prefix_state:
                ans = max(ans,i - prefix_state[mask])
            else:
                prefix_state[mask] = i
            
            # Case 2: exactly one digit odd
            for d in range(10):
                candidate = mask ^ (1 << d)
                if candidate in prefix_state:
                    ans = max(ans,i - prefix_state[candidate])
            
        return ans