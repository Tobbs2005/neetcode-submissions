class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        ans = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < curr[1]:
                #overlapping
                ans += 1
                if intervals[i][1] < curr[1]:
                    # take the shorter one
                    curr = intervals[i]
            else:
                # no overlap take next curr
                curr = intervals[i]
        return ans