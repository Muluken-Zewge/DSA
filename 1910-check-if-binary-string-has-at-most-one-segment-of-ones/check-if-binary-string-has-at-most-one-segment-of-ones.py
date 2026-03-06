class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        state = s[0]

        for ch in s[1:]:
            if state == '1' and ch == '0':
                state = '0'
            elif state == '0' and ch == '1':
                return False
            
        return True