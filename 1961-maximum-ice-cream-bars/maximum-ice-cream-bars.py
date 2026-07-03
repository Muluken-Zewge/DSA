class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cnt = max(costs)        
        count = [0] * (max_cnt+1)
        for c in costs:
            count[c] += 1

        total = 0
        ans = 0
        for cost,freq in enumerate(count):
            i = freq
            while i > 0:
                total += cost
                if total <= coins:
                    ans += 1
                i -= 1
            if total > coins:
                break
        
        return ans