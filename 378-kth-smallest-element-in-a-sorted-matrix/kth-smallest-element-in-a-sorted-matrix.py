class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [] 
        for i in range(n):
            for j in range(n):
                heappush(heap, -matrix[i][j])
                
                if len(heap) > k:
                    heappop(heap)
        
        return -heap[0]