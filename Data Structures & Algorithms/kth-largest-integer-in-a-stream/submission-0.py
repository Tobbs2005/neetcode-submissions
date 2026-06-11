class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        heapq.heapify(self.minheap)
        for num in nums:
            heapq.heappush(self.minheap, num)
            if len(self.minheap) > k:
                heapq.heappop(self.minheap)
        
        self.k = k


    def add(self, val: int) -> int:
        
        heapq.heappush(self.minheap, val)
        if len(self.minheap)> self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]



        

