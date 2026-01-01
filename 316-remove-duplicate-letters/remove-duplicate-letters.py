class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = Counter(s)

        for char in s:
            count[char] -= 1
            if char in stack:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return "".join(stack)
