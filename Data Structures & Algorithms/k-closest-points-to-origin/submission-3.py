class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, y1, x2, y2):
            return (x1 - x2)**2 + (y1 - y2)**2
        
        heap = []
        heapq.heapify(heap)
        for point in points:
            d = distance(0, 0, point[0], point[1])
            heapq.heappush(heap, (d, point[0], point[1]))
        
        ans = []

        for i in range(k):
            p = heapq.heappop(heap)
            ans.append([p[1], p[2]])
        
        return ans
        