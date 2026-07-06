class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removals = 0
        prev_s = intervals[0][0]
        prev_e = intervals[0][1]

        for curr_s, curr_e in intervals[1:]:
            if curr_e <= prev_e: # current interval removal
                removals += 1
            else:
                if prev_s == curr_s and prev_e <= curr_e: # previous interval removal
                    removals += 1
                
                prev_s = curr_s
                prev_e = curr_e
        
        return len(intervals) - removals