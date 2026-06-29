class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        greater = []
        equal = []

        for n in nums:
            if n < pivot:
                smaller.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                equal.append(n)
        
        return smaller + equal + greater