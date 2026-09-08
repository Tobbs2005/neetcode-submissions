class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        def isOverlap(a, b):
            return a[0] <= b[1] or a[1] <= b[0]
        
        res = []

        res.append(intervals[0])
        for i in range(1, len(intervals)):

            if isOverlap(intervals[i], res[-1]):

                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return res

