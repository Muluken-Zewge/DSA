class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        spec_pos = 0
        col_1 = defaultdict(int) # store number of 1's in each column
        row_1 = defaultdict(int) # store number of 1's in each row

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    row_1[i] += 1
                    col_1[j] += 1
        
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    if row_1[i] == 1 and col_1[j] == 1:
                        spec_pos += 1
        
        return spec_pos