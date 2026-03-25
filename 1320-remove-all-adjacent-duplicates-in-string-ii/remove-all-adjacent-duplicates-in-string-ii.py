class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] == k-1:
                i = k - 1
                while i > 0:
                    stack.pop()
                    i -= 1
            else:
                if stack and stack[-1][0] == c:
                    cnt = stack[-1][1]
                    stack.append((c,cnt+1))
                else:                    
                    stack.append((c,1))
        ans = ''
        for c,_ in stack:
            ans += c
            
        return ans