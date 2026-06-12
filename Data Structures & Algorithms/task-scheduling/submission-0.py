class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        #max heap to store most occurring
        hashmap = defaultdict(int)
        for task in tasks:
            hashmap[task] += 1
        
        for letter, count in hashmap.items():
            heapq.heappush(heap, [-count, letter])
        time = 0
        cooldown = []
        while cooldown or heap:
            time += 1
            if not heap:
                time = cooldown[0][1]
            if cooldown:
                if cooldown[0][1] == time:
                    heapq.heappush(heap, cooldown[0][0])
                    del cooldown[0]
            if heap:
                curr = heapq.heappop(heap)
                curr[0] += 1
                if curr[0] < 0:
                    cooldown.append([curr, time+n+1])
        return time


        