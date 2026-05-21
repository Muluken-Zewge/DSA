class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (char,val)
        ans = []

        for char in s:
            if stack and stack[-1][0] == char:
                freq = stack[-1][1]
                if freq + 1 == k:
                    while freq > 0:
                        stack.pop()
                        freq -= 1
                else:
                    stack.append((char,freq+1))
            else:
                stack.append((char,1))
        
        ans = [c for c,_ in stack]

        return "".join(ans)