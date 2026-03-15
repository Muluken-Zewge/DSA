class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        def dfs(r,c,tracker):
            if (r < 0 or r >= n) or (c < 0 or c >= m):
                return
            if board[r][c] == "X":
                return
            if (r == 0 or r == n-1) or (c == 0 or c == m-1):
                tracker["surrounded"] = False
            board[r][c] = "X"
            tracker["indices"].append((r,c))

            dfs(r+1,c,tracker)
            dfs(r-1,c,tracker)
            dfs(r,c+1,tracker)
            dfs(r,c-1,tracker)

        for r in range(n):
            for c in range(m):
                if board[r][c] == "O":
                    tracker = {
                        "surrounded": True,
                        "indices": []
                    }
                    dfs(r,c,tracker)
                    if tracker["surrounded"] == False:
                        for i,j in tracker["indices"]:
                            board[i][j] = "O"

        