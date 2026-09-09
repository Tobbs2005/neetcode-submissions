"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])


        p1 = 0
        p2 = 0

        res = 0
        n = len(intervals)
        curr = 0
        while p1 < n:
            if start[p1] < end[p2]:
                curr += 1
                p1 += 1
                res = max(curr, res)
            else:
                curr -= 1
                p2 += 1
        


        return res

