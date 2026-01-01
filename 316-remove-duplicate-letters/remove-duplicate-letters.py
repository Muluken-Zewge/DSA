class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        # to check if char exists to the right of the current char
        count = Counter(s) 
        seen = set() # to check duplicate

        for char in s:
            count[char] -= 1
            if char in seen:
                continue
            # if current char is smaller than chars in the stack and we can find them later, pop them out
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return "".join(stack)
