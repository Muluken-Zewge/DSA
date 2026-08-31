'''the dp approach is not optimised. so we go with the greedy one. the key is to see the problem as layer problem like kind of a bfs problem. we treat ranges in a jump together. we first process how far we reach with our next jump, then when we make the jump, that's the information we use. so we process -> we jump.
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0 # number of jumps we already made
        max_reach = 0 # the furthest we can reach from our current range
        curr_end = 0 # the end of the range we're processing

        for i in range(n):
            max_reach = max(max_reach, i + nums[i])

            if i == curr_end: # end of range
                jumps += 1
                curr_end = max_reach
                if curr_end >= n -1:
                    break
        
        return jumps