class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(rate, hours):
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            return time <= hours
        
        l = 1
        r = max(piles)
        # F F F T T T first true
        while l < r:
            mid = (l+r) // 2
            if canEat(mid, h):
                r = mid
            else:
                l = mid + 1
        return l
