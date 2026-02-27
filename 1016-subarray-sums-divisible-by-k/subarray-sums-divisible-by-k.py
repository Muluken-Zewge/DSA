class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """ this is also a prefix difference pattern just like 560.
        this time, we track the remainder and if a prefix sum equal to 
        the  remainder exists,that means removing that prefix would make
        the current prefix remainder a zero->sub array between the two
        indices is divisible by k. 
        """

        curr_sum = 0
        ans = 0
        prefix_map = defaultdict(int) 
        prefix_map[0] = 1 # base case: for subarrays starting from index 0

        for n in nums:
            curr_sum += n
            remain = curr_sum % k
            ans += prefix_map[remain]
            prefix_map[remain] += 1
        
        return ans