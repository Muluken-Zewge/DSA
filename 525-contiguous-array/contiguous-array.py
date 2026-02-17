class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # using prefix difference pattern
        ans = 0
        diff = 0
        diff_map = {0:-1} # {diff:index}

        for i in range(len(nums)):
            if nums[i] == 1:
                diff += 1
            else:
                diff -= 1
            
            if diff in diff_map:
                ans = max(ans,i - diff_map[diff])
            else:
                diff_map[diff] = i
        
        return ans