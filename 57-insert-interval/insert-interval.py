class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort()
        ans = []

        for start,end in intervals:
            if not ans or start > ans[-1][1]:
                ans.append([start,end])
            else:
                ans[-1][1] = max(ans[-1][1],end)
        
        return ans