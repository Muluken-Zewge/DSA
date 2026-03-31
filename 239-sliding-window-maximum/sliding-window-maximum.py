class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        queue = deque()
        ans = []

        while r < len(nums):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])
            
            if r - l + 1 > k:
                if nums[l] == queue[0]:
                    queue.popleft()
                l += 1
            if r - l + 1 == k:
                ans.append(queue[0])

            r += 1
        
        return ans