class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def isOverlap(a, b):
            return a[1] > b[0] and a[0] < b[1]
        intervals.sort()
        print(intervals)
        print(isOverlap([1,2], [2,4]))
        curr = 0
        res = 0
        for i in range(1, len(intervals)):
            
            if isOverlap(intervals[curr], intervals[i]):
          
                #remove bigger end
                # set curr to the smaller end and increment
                res += 1
                if intervals[curr][1] > intervals[i][1]:
                    curr = i
            else:
                #no overlap
                curr = i
        return res


