class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False
        
        phase = -1  #0 = inc, 1 = dec, 2 = inc
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return False
            
            if phase == -1:
                if nums[i] > nums[i-1]:
                    phase = 0
                else:
                    return False

            elif phase == 0:
                if nums[i] < nums[i-1]:
                    phase = 1
            elif phase == 1:
                if nums[i] > nums[i-1]:
                    phase = 2
            else: # phase = 2
                if nums[i] < nums[i-1]:
                    return False
            
        return phase == 2