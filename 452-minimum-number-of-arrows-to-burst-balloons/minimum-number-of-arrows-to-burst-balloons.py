class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev_end = points[0][1]
        arrows = 1

        for start,end in points[1:]:
            # if there is no overal, increment arrows
            if start > prev_end:
                arrows += 1
                prev_end = end
            else:
                prev_end = min(prev_end, end)

        return arrows  