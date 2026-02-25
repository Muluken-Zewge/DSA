class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # before the single number occurs, the starting index of the pair is even and the ending index is odd
        # after the single number, the strting index is odd and the ending is even

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if mid % 2 == 0:
                # correct pattern(even,odd) -> shring to the right
                if nums[mid] == nums[mid+1]:
                    left = mid + 1
                else:#(odd,even)->single number exists ->shrink to left
                    right = mid
            else:
                # correct pattern(even,odd) -> shring to the right
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:#(odd,even)->single number exists ->shrink to left
                    right = mid
        
        return nums[left]