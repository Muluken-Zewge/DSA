class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r,c):
            if not (0 <= r < m and 0 <= c < n):
                return 0
            if grid[r][c] == 0:
                return 0

            # mask as visited
            grid[r][c] = 0

            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
        
        max_area = 0
        for r in range(m):
            for c in range(n):
                print(r,c)
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area