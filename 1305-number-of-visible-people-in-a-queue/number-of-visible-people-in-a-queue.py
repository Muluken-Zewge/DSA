class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """we use montonically decreasing stack iterating from right to
        left.
        if there's anyone taller than you colser to the left, you are
        guarated not be seen by anyone to the left of that index.for every
        index, you pop shorter people since you can see them, and check if
        there's a remaining element in the stack, only tallers people
        blocking you not see the people after them can exist, but you can
        see them so you also count them.
        """
        n = len(heights)
        ans = [0] * n
        stack = []
       
        for i in range(n-1,-1,-1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            if stack:
                count += 1
            stack.append(heights[i])
            ans[i] = count
        
        return ans