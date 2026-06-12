'''we compute both paths(water->land and land->water) and take the minimum. we calculate the earliest time we can finish starting from the land. then for that early land finish, we check all water paths for an early land to water finish. we do exactly the same for water to land finish. find early water finish -> iteratre over all land path and find the early water to land finish. then take the minimmun of the two.
'''
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        ans = float("inf")

        # find early land finsh
        early_land = float("inf")
        for i in range(n):
            early_land = min(early_land, landStartTime[i] + landDuration[i])
        
        # find early water finish
        early_water = float("inf")
        for i in range(m):
            early_water = min(early_water, waterStartTime[i] + waterDuration[i])
        
        # find the earliest land -> water path
        for i in range(m):
            curr_min = max(early_land, waterStartTime[i]) + waterDuration[i]
            ans = min(ans, curr_min)
        
        # find the earliest water -> land path
        for i in range(n):
            curr_min = max(early_water, landStartTime[i]) + landDuration[i]
            ans = min(ans, curr_min)
        
        return ans