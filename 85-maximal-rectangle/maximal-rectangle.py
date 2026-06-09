'''for every row, we assume that row is the bottom of the rectangle, build histogram of heights and compute largest rectangle just like Largest Rectangle in Histogram problem. when we form the histogram, the height will be the number of consecutive ones from top to to that row, if there is a 0, the height is reseted to 0 at that position.
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        # function to find the largest rectangle in histogram
        def largestRectangle(heights: List[int]) -> int:
            max_area = 0
            stack = [] #(index,height)

            for i,h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index,height = stack.pop()
                    max_area = max(max_area, height *(i-index))
                    start = index
                stack.append((start,h))
            
            for i,h in stack:
                width = len(heights) - i
                max_area = max(max_area, h * width)
            
            return max_area

        heights = [0] * len(matrix[0])
        ans = 0

        for row in matrix:

            # Update histogram
            for i in range(len(row)):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            ans = max(ans, largestRectangle(heights))
        
        return ans