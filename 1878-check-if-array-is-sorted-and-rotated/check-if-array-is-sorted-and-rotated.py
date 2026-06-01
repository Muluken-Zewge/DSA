class Solution:
    def check(self, nums: List[int]) -> bool:
        # if there is more than 1 drop in the rotation, it is not sorted
        n = len(nums)
        drops = 0
        
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                drops += 1
        
        return drops <= 1