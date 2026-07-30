class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        nums = set(nums)
        for n in range(1,n+1):
            if n not in nums:
                ans.append(n)
        
        return ans