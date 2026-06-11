class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap and remove max elements
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]