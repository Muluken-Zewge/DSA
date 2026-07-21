class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        ans = []
        current = []

        def backtrack(index):
            if index == len(digits):
                ans.append("".join(current))
                return
            
            for letter in phone[digits[index]]:
                current.append(letter)
                backtrack(index + 1)
                current.pop()
        
        backtrack(0)
        return ans