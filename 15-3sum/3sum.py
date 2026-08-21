class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        for i in range(len(nums)):
            target = -1 * nums[i]
            seen = set()
            for n in nums[i+1:]:
                diff = target - n
                if diff in seen:
                    ans.add(tuple(sorted([nums[i],diff,n])))
                seen.add(n)
        
        return [list(triplet) for triplet in ans]