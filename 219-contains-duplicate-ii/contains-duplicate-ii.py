class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tracker = {}

        for i,val in enumerate(nums):
            if val in tracker:
                if i - tracker[val] <= k:
                    return True
        
            tracker[val] = i
        
        return False