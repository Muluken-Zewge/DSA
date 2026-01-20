class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        a = 0 # alice pointer
        b = 1 # bob pointer
        ans = []
        n = len(nums)
        while a < n and b < n:
            ans.append(nums[b])
            ans.append(nums[a])
            a += 2
            b += 2
        
        return ans