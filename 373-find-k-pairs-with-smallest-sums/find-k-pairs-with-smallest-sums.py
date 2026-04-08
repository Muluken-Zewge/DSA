class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i in range(min(k,len(nums1))):
            heappush(heap,(nums1[i]+nums2[0],i,0))
        
        while heap and len(ans) < k:
            _,i,j = heappop(heap)
            ans.append([nums1[i],nums2[j]])
            if j + 1 < len(nums2):
                heappush(heap, (nums1[i]+nums2[j+1],i,j+1))
        
        return ans