class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        common_cnt = 0
        seen = set()
        ans = [0] * n

        for i in range(n):
            if A[i] in seen:
                common_cnt += 1
            else:
                seen.add(A[i])
            if B[i] in seen:
                common_cnt += 1
            else:
                seen.add(B[i])
                
            ans[i] = common_cnt
        
        return ans