class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        """we start from the edge 'O's and mark all their neighbours '#' to
        mark them back to 'O' since they're guarnteed to be not surrounded.
        the untouched 'O's in this process are guaranted to be surrounded.
        """
        n, m = len(board), len(board[0])

        def dfs(r,c):
            if (r < 0 or r >= n) or (c < 0 or c >= m):
                return
            if board[r][c] != "O":
                return
            
            board[r][c] = "#"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        # mark boarder-connected 'O's
        for r in range(n):
            dfs(r,0) # left border
            dfs(r,m-1) # right border
        for c in range(m):
            dfs(0,c) # top border
            dfs(n-1,c) # bottom border
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"