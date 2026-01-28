class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = [[arr[0],arr[1]]]
        min = arr[1] - arr[0]

        for i in range(1,len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff == min:
                ans.append([arr[i],arr[i+1]])
            elif diff < min:
                while ans and diff < min:
                    ans.pop()
                ans.append([arr[i],arr[i+1]])
                min = diff

        return ans