class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l_heap = [] # max heap
        r_heap = [] # min heap
        nums1 += nums2

        for n in nums1:
            if not l_heap or n < -l_heap[0]:
                heappush(l_heap,-n)
            else:
                heappush(r_heap,n)

            if len(l_heap) > len(r_heap) + 1:
                heappush(r_heap,-heappop(l_heap))
            elif len(r_heap) > len(l_heap) + 1:
                heappush(l_heap,-heappop(r_heap))
                
        if len(l_heap) > len(r_heap):
            return -l_heap[0]
        elif len(r_heap) > len(l_heap):
            return r_heap[0]
        else:
            return (-l_heap[0] + r_heap[0]) / 2