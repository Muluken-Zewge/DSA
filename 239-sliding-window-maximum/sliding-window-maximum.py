class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = 0 # left pointer
        ans = []

        for r in range(len(nums)):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            if r - l + 1 == k:
                ans.append(queue[0])
                if nums[l] == queue[0]:
                    queue.popleft()
                l += 1
        
        return ans