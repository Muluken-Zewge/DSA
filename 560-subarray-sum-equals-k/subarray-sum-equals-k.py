class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """ another variation of prefix difference pattern(track prefix state in hashmap). we track the number of times a prefix sum occured.
        """
        ans = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        for n in nums:
            prefix_sum += n
            diff = prefix_sum - k

            if diff in prefix_map:
                ans += prefix_map[diff]
                
            prefix_map[prefix_sum] += 1

        return ans