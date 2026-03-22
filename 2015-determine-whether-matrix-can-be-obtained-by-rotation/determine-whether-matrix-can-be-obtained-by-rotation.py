class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate(matrix):
            new = [[0]* n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    new[j][n-1-i] = matrix[i][j]
            return new
        
        # rotate 0,90,180,270 degrees
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False