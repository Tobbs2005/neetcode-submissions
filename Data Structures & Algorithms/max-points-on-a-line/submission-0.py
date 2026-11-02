from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, n):
                x2, y2 = points[j][0], points[j][1]

                dy = y2-y1
                dx = x2-x1

                g = gcd(dy, dx)
                dy //= g
                dx //= g

                if dx < 0 or (dx == 0 and dy < 0):
                    dy, dx = -dy, -dx

                slopes[(dy, dx)] += 1
                res = max(res, slopes[(dy, dx)])
        return res + 1






