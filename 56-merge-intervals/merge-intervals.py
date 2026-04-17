class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals
    
        intervals.sort()
        ans = []
        prev_s = intervals[0][0]
        prev_e = intervals[0][1]

        for i in range(1,n):
            curr_s = intervals[i][0]
            curr_e = intervals[i][1]

            # overlap
            if curr_s <= prev_e:
                if curr_e > prev_e:
                    prev_e = curr_e
            else: 
                ans.append([prev_s,prev_e])
                prev_s = curr_s
                prev_e = curr_e
            if i == n-1:
                ans.append([prev_s,prev_e])
       
        return ans