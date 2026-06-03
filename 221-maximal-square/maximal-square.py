'''we assume each cell to be the top left corner of a potential square and evaluate the right, bottom and bottom-right(diagonal). we use bottom-up DP to get previously computed values easily.
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # stores the lenght(not the area) of the largest square that can be formed making matrix[i][j] the top left corner 
        dp = [[0] * n for _ in range(m)] 

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                right = dp[r][c+1] if c+1 < n else 0
                bottom = dp[r+1][c] if r+1 < m else 0
                diagonal = dp[r+1][c+1] if (r+1 < m and c+1 < n) else 0
                num = int(matrix[r][c])
                dp[r][c] = 0 if num == 0 else num + min(right,bottom,diagonal)

        max_length = max(max(r) for r in dp)

        return max_length ** 2