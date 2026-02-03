class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        status = [] # 1 for increasing, 0 for decreasing
        stack = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > stack[-1]:
                if not status or status[-1] != 1:
                    status.append(1)
                stack.append(nums[i])
            elif nums[i] < stack[-1]:
                if not status or status[-1] != 0:
                    status.append(0)
                stack.append(nums[i])
            else:
                return False
                
        return status == [1,0,1]