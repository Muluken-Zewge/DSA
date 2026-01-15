class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] # to store the score
        
        for char in s:
            if char == ')':
                val = stack.pop()
                if val == 0: # find opened bracket(not nested)
                    stack[-1] += 1
                else: # nested 
                    stack[-1] += 2 * val
            else:
                stack.append(0)

        return stack[0]
