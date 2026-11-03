class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we need the left and right next smaller element
        # at each index, with height h, the largest histogram of h is till next smaller element on left and right

        # two pass to build array
        # one pass to find max
        n = len(heights)
        right = [n] * n
        mono = []
        for i in range(n):
            while mono and heights[mono[-1]] > heights[i]:
                right[mono[-1]] = i
                mono.pop()
            mono.append(i)


        # left pass
        left = [-1] * n
        mono = []
        for i in range(n-1, -1, -1):
            while mono and heights[mono[-1]] > heights[i]:
                left[mono[-1]] = i
                mono.pop()
            mono.append(i)
        
        res = 0
        for i in range(n):
            curr = heights[i] * ((right[i]-1) - (left[i]+1) + 1)

            res = max(res, curr)
        return res

        
