class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # use sliding window with two monotonic queues(increasing & decreasing)
        l = 0 # left pointer
        longest = 0
        maxq = deque() # decreasing to keep track of the max in the window
        minq = deque() # increasing to keep track of the min in the window

        for r in range(len(nums)):
            # populate the max queue
            while maxq and maxq[-1] < nums[r]:
                maxq.pop()
            maxq.append(nums[r]) 

             # populate the min queue
            while minq and minq[-1] > nums[r]:
                minq.pop()
            minq.append(nums[r])

            # check for shrinking condition
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[l]:
                    maxq.popleft()
                if minq[0] == nums[l]:
                    minq.popleft()
                l += 1
            
            # update the longest subarray
            longest = max(longest, r-l+1)
        
        return longest