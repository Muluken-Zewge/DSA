class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # pure math approach
        n = len(digits)
        num = 0
        base = 0
        for i in range(n-1,-1,-1):
            num += digits[i] * 10 ** base
            base += 1
        num += 1
        ans = []
        while num > 0:
            ans.append(num%10)
            num //= 10
        
        return ans[::-1]