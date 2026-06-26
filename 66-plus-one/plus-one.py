class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # pure math approach
        # n = len(digits)
        # num = 0
        # base = 0
        # for i in range(n-1,-1,-1):
        #     num += digits[i] * 10 ** base
        #     base += 1
        # num += 1
        # ans = []
        # while num > 0:
        #     ans.append(num%10)
        #     num //= 10
        
        # return ans[::-1]

        # -- dsa approach --
        rem = 1
        ans = []
        for i in range(len(digits)-1,-1,-1):
            if digits[i] + rem == 10:
                ans.append(0)
            else:
                ans.append(digits[i]+rem)
                rem = 0
        if rem == 1:
            ans.append(rem)
        
        return ans[::-1]