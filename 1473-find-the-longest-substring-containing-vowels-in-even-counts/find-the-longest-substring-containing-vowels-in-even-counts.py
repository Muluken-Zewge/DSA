class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """we track vowel occurances with 1(odd) and 0(even).we use 5 bits
        for the 5 vowels(0->'a',1->'e',2->'i',3->'o',4->'u'). use
        bitmask to update the state and a map to track the state while
        iterating over the string(prefix difference pattern)
        """
        vowel_map = {'a': 0,'e': 1,'i': 2,'o': 3,'u': 4}
        prefix_map = {0:-1} # base case:empty prefix
        mask = 0
        longest = 0

        for i, ch in enumerate(s):
            if ch in vowel_map:
                mask ^= (1 << vowel_map[ch]) # flip the bit of the vowel
            
            if mask in prefix_map:
                longest = max(longest,i - prefix_map[mask])
            else:
                prefix_map[mask] = i

        return longest