class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = arr.copy()
        sorted_arr.sort()
        val_idx = {}
        i = 0
        for n in sorted_arr:
            if n not in val_idx:
                val_idx[n] = i
                i += 1

        ans = [0] * len(arr)
        for i,n in enumerate(arr):
            idx = val_idx[n]
            ans[i] = idx + 1
    
        return ans