class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)

        min_sum = nums[0]
        arr = nums[1:]
        arr.sort()
        min_sum += arr[0]
        min_sum += arr[1]

        return min_sum