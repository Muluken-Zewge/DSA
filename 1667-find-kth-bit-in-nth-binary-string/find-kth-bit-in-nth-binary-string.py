class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(s):
            res = ''
            for c in s:
                if c == '0':
                    res += '1'
                else:
                    res += '0'
            return res

        def dfs(n):
            if n == 1:
                return "0"
           
            return dfs(n-1) + '1' + "".join(reversed(invert(dfs(n-1))))
        
        s = dfs(n)
        return s[k-1]