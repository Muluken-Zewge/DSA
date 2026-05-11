class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        prefix_state = {0:1} # mask 0 occur one time in empty string
        mask = 0
        count = 0

        for char in word:
            idx = ord(char) - ord('a')
            mask ^= (1 << idx)

            # Case 1: all even
            count += prefix_state.get(mask,0)
            
            # Case 2: exactly one odd
            for b in range(10):
                candidate = mask ^ (1 << b)
                count += prefix_state.get(candidate,0)
            
            # update frequency
            prefix_state[mask] = prefix_state.get(mask,0) + 1
        
        return count