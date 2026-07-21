class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #product of all numbers before current index(excluding current index)
        prefix_prod = [1] * n 

        for i in range(1,n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        
        suffix_prod = 1
        ans = prefix_prod
        for i in range(n-1,-1,-1):
            ans[i] = prefix_prod[i] * suffix_prod 
            suffix_prod *= nums[i]
        
        return ans