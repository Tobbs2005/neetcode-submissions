"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()

        # 0, 5, 15
        # 10, 20, 40
        n = len(intervals)
        s = 0
        e = 0
        curr = 0
        ans = 0
        while e < n:
            while s < n and start[s] < end[e]:
                curr += 1
                ans = max(ans, curr)
                s += 1
            e += 1
            curr -= 1
        return ans