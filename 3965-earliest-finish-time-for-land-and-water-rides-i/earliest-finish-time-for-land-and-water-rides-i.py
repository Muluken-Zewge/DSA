class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n , m = len(landStartTime), len(waterStartTime)
        ans = float("inf")
        # find earliest finish time from land
        early_land = 10 ** 4
        for i in range(n):
            early_land = min(early_land, landStartTime[i]+landDuration[i])

        # find total early finish starting from land
        for i in range(m):
            curr_ans = max(early_land,waterStartTime[i]) + waterDuration[i]
            ans = min(ans, curr_ans)
        
        # find earliest finish time from water
        early_water = 10 ** 4
        for i in range(m):
            early_water = min(early_water, waterStartTime[i]+waterDuration[i])
        
        # find total early finish starting from water
        for i in range(n):
            curr_ans = max(early_water,landStartTime[i]) + landDuration[i]
            ans = min(ans, curr_ans)
        
        return ans