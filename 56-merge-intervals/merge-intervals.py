class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        
        for start,end in intervals:
            # no overlap
            if not merged or start > merged[-1][1]:
                merged.append([start,end])
            else: # overlap
                merged[-1][1] = max(merged[-1][1],end)
        
        return merged