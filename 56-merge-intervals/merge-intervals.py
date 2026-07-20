class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        prev_s, prev_e = intervals[0][0], intervals[0][1]
        ans = []

        for curr_s,curr_e in intervals[1:]:
            if curr_s <= prev_e:
                prev_e = max(prev_e,curr_e)
            else:
                ans.append([prev_s,prev_e])
                prev_s = curr_s
                prev_e = curr_e
        ans.append([prev_s,prev_e])

        return ans