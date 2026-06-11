class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        

        while len(heap) > 1:
            one = -heapq.heappop(heap)
            two = -heapq.heappop(heap)
            if one != two:
                heapq.heappush(heap, -abs(one-two))
          
                

        if len(heap) == 0:
            return 0
        else:
            return -heap[0]
            
