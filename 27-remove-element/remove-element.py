class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        k = 0
        while l < r:  
            if nums[l] == val and nums[r] == val: 
                r -= 1
            elif nums[l] != val and nums[r] != val:
                l += 1
            elif nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            else:
                l += 1
                r -= 1
        
        val_count = nums.count(val)
             
        return n - val_count