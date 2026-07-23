class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = []
        ans = []

        def backtrack(first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for num in range(first_num,n+1):
                curr.append(num)
                backtrack(num+1)
                curr.pop()

        backtrack(1)
        return ans
