class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        bought = 0
        min_cost = 0
        cost.sort(reverse=True)

        for c in cost:
            if bought == 2:
                bought = 0
                continue
            else:
                min_cost += c
                bought += 1
        
        return min_cost