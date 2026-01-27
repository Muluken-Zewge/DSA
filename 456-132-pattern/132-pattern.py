class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = [] # monotonic decreasing stack to store the 3 in 132 pattern
        two = float("-inf") # the 2 in the 132 pattern

        for i in range(n-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                # we found legit 2
                two = stack.pop()
            # check if we find legit one
            if nums[i] < two:
                return True
            stack.append(nums[i])
        
        return False