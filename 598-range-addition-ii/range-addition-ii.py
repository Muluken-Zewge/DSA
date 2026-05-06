class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
            
        r = [cell[0] for cell in ops]
        c = [cell[1] for cell in ops]

        return min(r) * min(c)