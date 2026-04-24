class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''we use heap with greedy approach. we use a brick for all jumps
        by default and when we no longer have a brick, we assign a ladder
        for the largest jump. max heap to store the jumps.
        '''
        n = len(heights)
        max_heap = []

        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                # use a brick by default
                bricks -= diff
                heappush(max_heap, -diff) # record brick usage
                if bricks < 0:
                    # use ladder for the largest jump(top of heap)
                    if ladders > 0:
                        ladders -= 1
                        #refund the largest brick usage
                        bricks += -heappop(max_heap) 
                    else:
                        return i
        
        return n-1