class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''If two prefix sums leave the same remainder when divided by k,
        then the subarray between them is divisible by k.
        '''
        prefix_state = {0:1} # {prefix_sum:frequency}
        count = 0
        prefix_sum = 0

        for n in nums:
            prefix_sum += n
            mod = prefix_sum % k
            if mod in prefix_state:
                count += prefix_state[mod]
            
            prefix_state[mod] = prefix_state.get(mod,0) + 1
           
        return count