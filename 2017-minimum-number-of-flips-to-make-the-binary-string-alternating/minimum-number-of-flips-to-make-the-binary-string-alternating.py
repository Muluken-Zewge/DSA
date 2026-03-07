class Solution:
    def minFlips(self, s: str) -> int:
        """for any given string,we have only two alternating strings, one
        starting with '0',the other staring with '1'. Type-1 operation
        let's us take the string as a circular string, so we can take all
        possible variations of the cirular string of length s, count
        the number of flips we need to make it alternating, then take the
        minimum of all.kind of brute force with sliding window:)
        """

        n = len(s) # length of original string to determine window size
        s = s + s # to simulate circualr behaviour 
        alt1, alt2 = "", "" # the two variations of valid alternating string
        diff1,diff2 = 0, 0 # flips needed for alt1 and alt2 respectively
        res = n

        # populate the valid alternating strings
        for i in range(len(s)):
            alt1 += '0' if i % 2 == 0 else '1' # alt1 starts with '0
            alt2 += '1' if i % 2 == 0 else '0' # alt2 starts with '1'
        
        l = 0 # left pointer
        for r in range(len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            
            # shrink the window
            if (r - l + 1) > n:
                # update the impact of the bit lefted out from diff
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
            
            # update result
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
            
        return res