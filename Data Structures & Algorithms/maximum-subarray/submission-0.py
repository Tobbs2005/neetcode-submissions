class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0

        curr = 0
        ans = -float('inf')

        n = len(nums)

        while right < n:
            curr += nums[right]
            ans = max(ans, curr)
            if curr <=0:
                left = right + 1
                curr = 0
            right += 1
        return ans
            
            