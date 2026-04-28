'''we use a min heap to store the right half of the sorted array because we want to get the min value in O(1) and we store the left half with max heap because we want to get the max value in O(1) so that we can find the median in O(1). 
'''
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # add to max_heap by default
        heappush(self.max_heap, -num)

        # check order(all values in max_heap <= all values in min_heap)
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            heappush(self.min_heap, -heappop(self.max_heap))

        # check length and balance(length difference shouldn't be > 1)
        if len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            median = (-self.max_heap[0] + self.min_heap[0]) / 2
            return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()