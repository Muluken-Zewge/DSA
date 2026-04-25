class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        size = len(self.arr)
        middle_idx = size // 2
        if size % 2 == 0:
            median = (self.arr[middle_idx] + self.arr[middle_idx-1]) / 2
            return median
        else:
            return self.arr[middle_idx]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()