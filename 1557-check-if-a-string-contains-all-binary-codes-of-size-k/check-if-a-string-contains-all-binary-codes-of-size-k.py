class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique_sub_strings = set()
        i, j = 0, k
        
        while j <= len(s):
            
            if s[i:j] not in unique_sub_strings:
                unique_sub_strings.add(s[i:j])
            if len(unique_sub_strings) == 2**k:
                return True
            
            i += 1
            j += 1
        
        return False