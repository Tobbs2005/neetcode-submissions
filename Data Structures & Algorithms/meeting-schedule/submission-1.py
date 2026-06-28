"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key = lambda i : i.start)
        if not intervals:
            return True
        curr = intervals[0]
        for i in range(1, n):
            if curr.end > intervals[i].start:
                return False
            curr = intervals[i]
        return True
