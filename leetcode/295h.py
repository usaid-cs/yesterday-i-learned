import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []
        self.middles = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)  # This inserts `num` where it is "supposed" to be in self.nums.
        self.length += 1
        if self.length % 2:
            self.middles = [self.length // 2, self.length // 2]
        else:
            self.middles = [self.length // 2 - 1, self.length // 2]

    def findMedian(self) -> float:
        idx1, idx2 = self.middles
        return (self.nums[idx1] + self.nums[idx2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
