class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort()
        ans = [intervals[0]]

        for start,end in intervals[1:]:
            # no overlap -> append
            if start > ans[-1][1]:
                ans.append([start,end])
            else: # overlap -> update end if neccessary
                ans[-1][1] = max(ans[-1][1],end)
        
        return ans