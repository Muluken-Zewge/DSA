class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n , m = len(landStartTime), len(waterStartTime)
        ans = float("inf")
        # find earliest finish time from land
        earliest_land_finish = 10 ** 4
        for i in range(n):
            earliest_land_finish = min(earliest_land_finish, landStartTime[i]+landDuration[i])
        
         # find earliest finish time from water
        earliest_water_finish = 10 ** 4
        for i in range(m):
            earliest_water_finish = min(earliest_water_finish, waterStartTime[i]+waterDuration[i])

        # find total early finish starting from land
        for i in range(m):
            curr_ans = max(earliest_land_finish,waterStartTime[i]) + waterDuration[i]
            ans = min(ans, curr_ans)
        
        # find total early finish starting from water
        for i in range(n):
            curr_ans = max(earliest_water_finish,landStartTime[i]) + landDuration[i]
            ans = min(ans, curr_ans)
        
        return ans