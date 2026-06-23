class MedianFinder:

    def __init__(self):
        self.left = []
        #max heap
        self.right = []
        #min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)                          # tentatively to max-heap
        heapq.heappush(self.right, -heapq.heappop(self.left)) 
        lenL, lenR = len(self.left), len(self.right)
        if lenR - lenL == 2:
            minR = heapq.heappop(self.right)
            heapq.heappush(self.left, -minR)

    def findMedian(self) -> float:
        lenL, lenR = len(self.left), len(self.right)
        if lenL == lenR:
            maxL = -self.left[0]
            minR = self.right[0]
            return (maxL + minR) / 2
        return self.right[0]

        