'''we use monotonic stack to check if we can extend the current height to the right. if the curr height is greater or equal to the top of the stack, it means it can be extended. if not, it can't, so calculate the max area we can get from it and pop. then when push the curr height, the start index should be the last index you popped. that is the concept of extending to the left when we pop because for all the elements you popped, it is guaranted the curr height can be extenede to left upto that index. and if there are elements left in the stack, that means those elements can extend untill the end.
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index,height)

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i-index))
                start = index # extend left
            stack.append((start,h))
        
        for i,h in stack:
            width = len(heights) - i
            max_area = max(max_area,h * width)
        
        return max_area