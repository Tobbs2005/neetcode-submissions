class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sort = sorted(weights)
        n = len(weights)
        def canShip(x):
            count = 0
            curr = x
            for weight in weights:
                if curr - weight < 0:
                    count += 1
                    curr = x
                curr -= weight
            return count+1 <= days

                
        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l+r) // 2
            if not canShip(m):
                l = m + 1
            else:
                r = m
        return l

                


