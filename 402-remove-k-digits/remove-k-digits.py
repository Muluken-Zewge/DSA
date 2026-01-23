class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        removed = 0
        for n in num:
            n = int(n)
            while stack and stack[-1] > n and removed < k:
                stack.pop()
                removed += 1

            if len(stack) < len(num) - k:
                stack.append(n)
            else:
                removed += 1

        ans = []
        append = False
        # remove leading zero's
        for n in stack:
            if append or n > 0:
                ans.append(n) 
            if n > 0:
                append = True

        return "0" if not ans else "".join(str(n) for n in ans)