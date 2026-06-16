class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep track of max and min at each num

        n = len(nums)
        curMax = 1
        curMin = 1
        ans = nums[0]
        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            ans = max(curMax, ans)
        return ans