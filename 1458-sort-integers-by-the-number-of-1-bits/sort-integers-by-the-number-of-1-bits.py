class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = []
        temp = []
        for num in arr:
            temp.append((num.bit_count(),num))
        temp.sort()

        for _,num in temp:
            ans.append(num)
        
        return ans