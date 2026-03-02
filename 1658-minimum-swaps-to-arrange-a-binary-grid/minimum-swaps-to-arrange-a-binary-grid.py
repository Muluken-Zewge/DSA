class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: count trailing zeros for each row
        trailing = []
        for row in grid:
            count = 0
            for num in reversed(row):
                if num == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: fix each row from top to bottom
        for i in range(n):
            required = n - i - 1
            j = i
            
            # find first row with enough trailing zeros
            while j < n and trailing[j] < required:
                j += 1
            
            if j == n:
                return -1  # no valid row found
            
            # bring row j up to position i
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps