class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        # (time, node)
        seen = set()
        count = 0

        adj = defaultdict(list)
        for src, tar, time in times:
            adj[src].append((tar, time))
        
        while heap:
            currTime, currNode = heapq.heappop(heap)
            if currNode in seen:
                continue
            seen.add(currNode)
            
            if len(seen) == n:
                #finished
                return currTime
            for edge, edgeTime in adj[currNode]:
                newTime = currTime + edgeTime
                heapq.heappush(heap, (newTime, edge))
        return -1



