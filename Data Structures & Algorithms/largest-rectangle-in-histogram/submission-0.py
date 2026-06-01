class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # at each height the largest rectangle area is next shorter value to its left and right
        # we can run two passes, for next smaller value leftwards and rightwards
        n = len(heights)
        # we need the next smaller value
        # monotonicly increasing stack
        stack = []
        right = [n]*n
        for i, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                right[stack[-1]] = i
                del stack[-1]
            stack.append(i)

        # now we need a leftwards pass
        stack = []
        left = [-1]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                left[stack[-1]] = i
                del stack[-1]
            stack.append(i)
        ans = 0
        # now for each height, calculate max volume at that height by doign right-left+1 * height
        for i, h in enumerate(heights):
            w = right[i] - left[i] - 1
            ans = max(ans, w*h)
        return ans
        