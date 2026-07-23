class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []

        def backtrack(index,curr_sum):
            if curr_sum == target:
                ans.append(combination[:])
                return
            if curr_sum > target:
                return
            
            for i in range(index,len(candidates)):
                combination.append(candidates[i])
                backtrack(i,curr_sum + candidates[i])
                combination.pop()
        
        backtrack(0,0)
        return ans
